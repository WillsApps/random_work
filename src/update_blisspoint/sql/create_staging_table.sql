DROP TABLE IF EXISTS dbt_wburdett.aaa_impressions_backfill_2023_01_27_{version}_{index};
CREATE TABLE dbt_wburdett.aaa_impressions_backfill_2023_01_27_{version}_{index}(
    _loaded_from VARCHAR(255),
    _loaded_from_date DATE,
    _load_date DATE,

    local_date DATE,
    local_timestamp TIMESTAMP,

    "timestamp" TIMESTAMP,
    ip VARCHAR(64),
    network VARCHAR(64),
    isci VARCHAR(64),
    device VARCHAR(64),
    os VARCHAR(32),
    isp VARCHAR(128),
    cost NUMERIC(24,20),
    zip VARCHAR(16),
    creative VARCHAR(512),
    uuid VARCHAR(36),
    count INT,
    media_type VARCHAR(12),
    media_breakdown VARCHAR(10),
    _copy_into_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
