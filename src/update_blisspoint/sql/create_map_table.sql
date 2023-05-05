DROP TABLE IF EXISTS dbt_wburdett.aaa_impressions_map_2023_01_27_{version}_{index};
CREATE TABLE dbt_wburdett.aaa_impressions_map_2023_01_27_{version}_{index} (
    _loaded_from VARCHAR(255),
    _copy_into_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
