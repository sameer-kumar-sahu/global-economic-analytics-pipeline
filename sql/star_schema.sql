CREATE TABLE dim_country (
    country_id INT AUTO_INCREMENT PRIMARY KEY,
    country_name VARCHAR(100),
    country_code VARCHAR(10) UNIQUE
);

CREATE TABLE dim_indicator (
    indicator_id INT AUTO_INCREMENT PRIMARY KEY,
    indicator_name VARCHAR(100) UNIQUE
);

CREATE TABLE fact_economic_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_id INT,
    indicator_id INT,
    year INT,
    value DECIMAL(30,5),

    FOREIGN KEY (country_id)
        REFERENCES dim_country(country_id),

    FOREIGN KEY (indicator_id)
        REFERENCES dim_indicator(indicator_id)
);