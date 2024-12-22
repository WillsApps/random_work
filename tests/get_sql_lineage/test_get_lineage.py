import sqlparse

from src.get_sql_lineage.get_lineage import get_cleaned_statement, get_identifiers


def test_get_identifiers_case_one():
    statement = sqlparse.parse(
        """WITH source AS (\n    SELECT * FROM "hubspot"."email_campaigns"\n),\n\nfinal AS (\n    SELECT\n        -- keys/ids\n        id AS email_campaign_id,\n        uuid,\n        content_id,\n        app_id,\n        group_id,\n\n        -- timestamps and dates\n        received_at,\n        uuid_ts,\n        last_processing_state_change_at,\n        last_processing_finished_at,\n        last_processing_started_at,\n        scheduled_at,\n\n        -- metrics\n        -- renaming the fields to be inline with metrics used in email_sends model\n        -- and to resemble the metric names used in dbt_hubspot package\n        counters_suppressed AS suppresses,\n        counters_reply AS replies,\n        counters_dropped AS drops,\n        counters_sent AS sends,\n        counters_click AS clicks,\n        counters_unsubscribed AS unsubscribes,\n        counters_statuschange AS status_changes,\n        counters_bounce AS bounces,\n        counters_delivered AS deliveries,\n        counters_open AS opens,\n        counters_processed AS processes,\n        counters_deferred AS deferrals,\n        counters_mta_dropped AS mta_drops,\n        counters_spamreport AS spam_reports,\n\n        -- details\n        subject AS subject,\n        app_name,\n        name AS name,\n        type AS type,\n        processing_state,\n        num_included,\n        sub_type\n\n    FROM source\n)\n\nSELECT * FROM final"""
    )[0]
    expected = ["hubspot.email_campaigns"]
    actual = get_identifiers(statement)
    assert expected == actual


def test_get_identifiers_case_two():
    sql = """\nWITH\n    source AS (\n        SELECT *\n        FROM\n            "iosregistry"."order_completed"\n        WHERE\n              received_at >= current_date - interval '1 days'\n        \n          AND /* removes cases where users timestamp is before lower limit set. */\n    received_at > '2019-01-01' AND timestamp > '2019-01-01'\n    AND timestamp <= sysdate\n    /* removes edge cases where users have changed their device clock to a future time. */\n    AND received_at >= timestamp\n    ),\n\n    user_master_alias AS (\n        SELECT *\n        FROM "dbt_wburdett"."user_master_aliases"\n    ),\n\n    final AS (\n        SELECT\n            -- keys/ids\n            oc.id AS event_id,\n            oc.anonymous_id AS visitor_id,\n            oc.registry_id,\n            oc.order_id,\n            oc.cart_id,\n            -- Aliased user id, checked against user_master_aliases\n            COALESCE(uma.user_id, oc.user_id) AS user_id,\n\n            -- timestamp/dates\n            oc.timestamp AS event_at,\n            oc.received_at, -- here for assisting temporarily for performance query if needed\n\n            -- details\n            oc.event AS event_type,\n            oc.event_text AS event_name,\n            oc.context_device_type,\n            oc.coupon,\n            oc.currency,\n            json_parse(oc.products) AS products,\n            json_array_length(oc.products, TRUE) AS num_products,\n            COALESCE((json_extract_path_text(json_extract_array_element_text(oc.products, 1), 'brand') = 'Zola Invites + Paper'), FALSE) AS is_paper_order,\n\n            oc.referring_screen_name,\n            oc.referring_screen_type,\n\n            -- measures\n            oc.shipping,\n            oc.tax,\n            oc.payment_total AS total,\n            oc.discount,\n            oc.value\n\n        FROM\n            source oc\n                LEFT JOIN user_master_alias uma\n                                ON oc.anonymous_id = uma.visitor_id\n    )\n\nSELECT *\nFROM\n    final\n    """
    sql = sqlparse.format(sql, strip_comments=True).replace("\n", " ")
    while "  " in sql:
        sql = sql.replace("  ", " ").strip()
    statement = sqlparse.parse(sql)[0]
    expected = ["iosregistry.order_completed", "dbt_wburdett.user_master_aliases"]
    actual = get_identifiers(statement)
    assert expected == actual


def test_get_cleaned_statement():
    sql = """\nWITH\n    source AS (\n        SELECT *\n        FROM\n            "iosregistry"."order_completed"\n        WHERE\n              received_at >= current_date - interval '1 days'\n        \n          AND /* removes cases where users timestamp is before lower limit set. */\n    received_at > '2019-01-01' AND timestamp > '2019-01-01'\n    AND timestamp <= sysdate\n    /* removes edge cases where users have changed their device clock to a future time. */\n    AND received_at >= timestamp\n    ),\n\n    user_master_alias AS (\n        SELECT *\n        FROM "dbt_wburdett"."user_master_aliases"\n    ),\n\n    final AS (\n        SELECT\n            -- keys/ids\n            oc.id AS event_id,\n            oc.anonymous_id AS visitor_id,\n            oc.registry_id,\n            oc.order_id,\n            oc.cart_id,\n            -- Aliased user id, checked against user_master_aliases\n            COALESCE(uma.user_id, oc.user_id) AS user_id,\n\n            -- timestamp/dates\n            oc.timestamp AS event_at,\n            oc.received_at, -- here for assisting temporarily for performance query if needed\n\n            -- details\n            oc.event AS event_type,\n            oc.event_text AS event_name,\n            oc.context_device_type,\n            oc.coupon,\n            oc.currency,\n            json_parse(oc.products) AS products,\n            json_array_length(oc.products, TRUE) AS num_products,\n            COALESCE((json_extract_path_text(json_extract_array_element_text(oc.products, 1), 'brand') = 'Zola Invites + Paper'), FALSE) AS is_paper_order,\n\n            oc.referring_screen_name,\n            oc.referring_screen_type,\n\n            -- measures\n            oc.shipping,\n            oc.tax,\n            oc.payment_total AS total,\n            oc.discount,\n            oc.value\n\n        FROM\n            source oc\n                LEFT JOIN user_master_alias uma\n                                ON oc.anonymous_id = uma.visitor_id\n    )\n\nSELECT *\nFROM\n    final\n    """
    expected = (
        'WITH source AS (SELECT * FROM "iosregistry"."order_completed" WHERE '
        "received_at >= current_date - interval '1 days' AND received_at > "
        "'2019-01-01' AND timestamp > '2019-01-01' AND timestamp <= sysdate AND "
        "received_at >= timestamp), user_master_alias AS (SELECT * FROM "
        '"dbt_wburdett"."user_master_aliases"), final AS (SELECT oc.id AS event_id, '
        "oc.anonymous_id AS visitor_id, oc.registry_id, oc.order_id, oc.cart_id, "
        "COALESCE(uma.user_id, oc.user_id) AS user_id, oc.timestamp AS event_at, "
        "oc.received_at, oc.event AS event_type, oc.event_text AS event_name, "
        "oc.context_device_type, oc.coupon, oc.currency, json_parse(oc.products) AS "
        "products, json_array_length(oc.products, TRUE) AS num_products, "
        "COALESCE((json_extract_path_text(json_extract_array_element_text(oc.products, "
        "1), 'brand') = 'Zola Invites + Paper'), FALSE) AS is_paper_order, "
        "oc.referring_screen_name, oc.referring_screen_type, oc.shipping, oc.tax, "
        "oc.payment_total AS total, oc.discount, oc.value FROM source oc LEFT JOIN "
        "user_master_alias uma ON oc.anonymous_id = uma.visitor_id) SELECT * FROM "
        "final"
    )
    actual = get_cleaned_statement(sql).value
    assert expected == actual
