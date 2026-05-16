CREATE DATABASE economic_analytics;

CREATE TABLE countries (
    country_id INT AUTO_INCREMENT PRIMARY KEY,
    country_name VARCHAR(100),
    country_code VARCHAR(10),
    region VARCHAR(100),
    income_group VARCHAR(100)
);

CREATE TABLE indicators (
    indicator_id INT AUTO_INCREMENT PRIMARY KEY,
    indicator_name VARCHAR(255),
    indicator_code VARCHAR(50)
);

CREATE TABLE economic_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_id INT,
    indicator_id INT,
    year INT,
    value DECIMAL(20,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (country_id) REFERENCES countries(country_id),
    FOREIGN KEY (indicator_id) REFERENCES indicators(indicator_id)
);