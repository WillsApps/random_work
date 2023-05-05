INSERT INTO dbt_wburdett.aaa_impressions_map_2023_01_27_{version}_{index}(
    _loaded_from
)
VALUES
    (
        '{s3_key}'
    );

COPY dbt_wburdett.aaa_impressions_backfill_2023_01_27_{version}_{index}(
  "timestamp",
  ip,
  network,
  isci,
  device,
  os,
  isp,
  cost,
  zip,
  creative,
  uuid,
  count,
  media_type,
  media_breakdown
)
FROM
  '{s3_key}'
IAM_ROLE '{iam_role}'
REMOVEQUOTES
BLANKSASNULL
EMPTYASNULL
COMPUPDATE OFF
DELIMITER ','
IGNOREHEADER 1
TIMEFORMAT 'auto' GZIP;
