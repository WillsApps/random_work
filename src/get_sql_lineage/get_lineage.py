import json
from dataclasses import dataclass, field
from typing import List, Dict, Any, Tuple, Union

import sqlparse
from sqlparse.sql import TokenList, Statement, Identifier

#
# @dataclass
# class Model:
#     name: str
#     sql: str
#     statement: Statement = field(init=False)
#     identifiers: List[str] = field(init=False)
#
#     def __post_init__(self):
#         self.statement = sqlparse.parse(self.sql.replace('"beehive".', ""))
#         self.identifiers = get_identifiers(self.statement)


def get_cleaned_statement(sql: str) -> Statement:
    sql = sqlparse.format(sql, strip_comments=True).replace("\n", " ")
    while "  " in sql:
        sql = sql.replace("  ", " ").strip()
        sql = sql.replace("( ", "(").strip()
        sql = sql.replace(" )", ")").strip()
    return sqlparse.parse(sql)[0]


def get_sql(path: str) -> Dict[str, Dict[str, Union[str, Statement]]]:
    # sql = 'WITH source AS (\n    SELECT * FROM "beehive"."hubspot"."email_subscription_event_changes"\n),\n\nfinal AS (\n    SELECT\n        id,\n        received_at,\n        uuid,\n        caused_by_event_created,\n        email_subscription_event_id,\n        "timestamp" AS event_timestamp,\n        uuid_ts,\n        caused_by_event_id,\n        change,\n        change_type,\n        portal_id,\n        source,\n        subscription_id\n\n    FROM source\n)\n\nSELECT * FROM final'
    # sql = sql.replace('"beehive".',"")
    # return {"dbt.stg_hubspot__email_subscription_event_changes", {"sql": sql, "statement": sqlparse.parse(sql)[0]},
    # }

    with open(path, "r") as f:
        contents = json.loads(f.read())
    # root:nodes:model_name:compiled_code

    all_sql = {}
    for _def in contents["nodes"].values():
        name: str = _def["name"]
        schema: str = _def["schema"]
        try:
            raw_sql = _def["compiled_code"].replace('"beehive".', "")
            statement = sqlparse.parse(raw_sql)[0]
            sql = sqlparse.format(raw_sql, strip_comments=True)
            identifiers = get_identifiers(statement)
        except KeyError:
            print(f"Model: {name} doesn't have compiled")
            continue
        all_sql[f"{schema}.{name}"] = {
            "sql": raw_sql,
            # "statement": sqlparse.parse(sql)[0],
            "sources": identifiers,
        }
    # with open(
    #     "/Users/Shared/web/random_work/src/get_sql_lineage/queries.json", "w"
    # ) as f:
    #     f.write(json.dumps(all_sql))
    return all_sql


def get_identifiers(token_list: TokenList) -> List[str]:
    identifiers = []
    for token in token_list:
        if (
            isinstance(token, Identifier)
            and '"."' in token.value
            and len(token.tokens) == 3
        ):
            identifiers.append(token.value.replace('"', ""))
        elif isinstance(token, TokenList):
            identifiers.extend(get_identifiers(token))
    return identifiers


def main():
    _all = get_sql("/Users/Shared/web/random_work/src/get_sql_lineage/manifest.json")

    # statement: Statement = _all[list(_all.keys())[0]]["statement"]

    # for t in statement.tokens:
    # identifiers = get_identifiers(statement)
    with open(
        "/Users/Shared/web/random_work/src/get_sql_lineage/lineage.json", "w"
    ) as f:
        f.write(json.dumps(_all, indent=2))
    print(_all)


if __name__ == "__main__":
    main()
