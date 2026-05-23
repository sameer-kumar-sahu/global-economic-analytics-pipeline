-- Latest GDP Ranking
SELECT
    country,
    year,
    ROUND(value / 1000000000000, 2) AS gdp_trillion_usd
FROM economic_data
WHERE indicator = 'GDP'
  AND year = (
        SELECT MAX(year)
        FROM economic_data
        WHERE indicator = 'GDP'
    )
ORDER BY gdp_trillion_usd DESC;


-- Average Inflation by Country
SELECT
    country,
    ROUND(AVG(value), 2) AS avg_inflation
FROM economic_data
WHERE indicator = 'Inflation'
GROUP BY country
ORDER BY avg_inflation DESC;


-- Population Growth Over Time
SELECT
    country,
    MIN(year) AS start_year,
    MAX(year) AS end_year,
    MIN(value) AS start_population,
    MAX(value) AS latest_population,
    MAX(value) - MIN(value) AS population_growth
FROM economic_data
WHERE indicator = 'Population'
GROUP BY country
ORDER BY population_growth DESC;


-- Star Schema Join Query
SELECT
    c.country_name,
    i.indicator_name,
    f.year,
    f.value
FROM fact_economic_data f
JOIN dim_country c
    ON f.country_id = c.country_id
JOIN dim_indicator i
    ON f.indicator_id = i.indicator_id
WHERE i.indicator_name = 'GDP'
ORDER BY f.year DESC, f.value DESC;


-- Latest Forecast GDP by Country
SELECT
    country,
    year,
    ROUND(forecast_value / 1000000000000, 2) AS forecast_gdp,
    model_name
FROM economic_forecast
WHERE indicator = 'GDP'
  AND year = (SELECT MAX(year) FROM economic_forecast WHERE indicator = 'GDP')
ORDER BY forecast_gdp DESC;


-- Actual GDP vs Forecast GDP Difference
SELECT
    a.country,
    a.year AS actual_year,
    a.value AS latest_actual_gdp,
    f.year AS forecast_year,
    f.forecast_value AS forecast_gdp,
    f.forecast_value - a.value AS gdp_difference,
    ROUND(((f.forecast_value - a.value) / a.value) * 100, 2) AS gdp_difference_percent
FROM economic_data a
JOIN economic_forecast f
    ON a.country = f.country
WHERE a.indicator = 'GDP'
  AND f.indicator = 'GDP'
  AND a.year = (SELECT MAX(year) FROM economic_data WHERE indicator = 'GDP')
  AND f.year = (SELECT MAX(year) FROM economic_forecast WHERE indicator = 'GDP')
ORDER BY gdp_difference DESC;


-- Forecast Growth by Country
SELECT
    country,
    indicator,
    MIN(year) AS forecast_start_year,
    MAX(year) AS forecast_end_year,
    MIN(forecast_value) AS start_forecast_value,
    MAX(forecast_value) AS end_forecast_value,
    MAX(forecast_value) - MIN(forecast_value) AS forecast_growth,
    ROUND(((MAX(forecast_value) - MIN(forecast_value)) / MIN(forecast_value)) * 100, 2) AS forecast_growth_percent
FROM economic_forecast
GROUP BY country, indicator
ORDER BY forecast_growth_percent DESC;


-- GDP Rank Change: Actual vs Forecast
WITH actual_rank AS (
    SELECT
        country,
        value AS actual_gdp,
        RANK() OVER (ORDER BY value DESC) AS actual_rank
    FROM economic_data
    WHERE indicator = 'GDP'
      AND year = (SELECT MAX(year) FROM economic_data WHERE indicator = 'GDP')
),
forecast_rank AS (
    SELECT
        country,
        forecast_value AS forecast_gdp,
        RANK() OVER (ORDER BY forecast_value DESC) AS forecast_rank
    FROM economic_forecast
    WHERE indicator = 'GDP'
      AND year = (SELECT MAX(year) FROM economic_forecast WHERE indicator = 'GDP')
)
SELECT
    a.country,
    a.actual_gdp,
    CAST(a.actual_rank AS SIGNED) AS actual_rank,
    f.forecast_gdp,
    CAST(f.forecast_rank AS SIGNED) AS forecast_rank,
    CAST(a.actual_rank AS SIGNED) - CAST(f.forecast_rank AS SIGNED) AS rank_change
FROM actual_rank a
JOIN forecast_rank f
    ON a.country = f.country
ORDER BY forecast_rank;
-- positive = country moved up in forecast
-- negative = country moved down
-- 0 = no rank change



-- Highest Inflation Year per Country
WITH inflation_rank AS (
    SELECT
        country,
        year,
        value AS inflation_rate,
        RANK() OVER (
            PARTITION BY country
            ORDER BY value DESC
        ) AS inflation_rank
    FROM economic_data
    WHERE indicator = 'Inflation'
)
SELECT
    country,
    year,
    inflation_rate
FROM inflation_rank
WHERE inflation_rank = 1
ORDER BY inflation_rate DESC;



-- Country Economic Summary
SELECT
    country,
    MAX(CASE WHEN indicator = 'GDP' THEN value END) AS latest_gdp,
    MAX(CASE WHEN indicator = 'Population' THEN value END) AS latest_population,
    ROUND(AVG(CASE WHEN indicator = 'Inflation' THEN value END), 2) AS avg_inflation
FROM economic_data
WHERE year = (SELECT MAX(year) FROM economic_data)
   OR indicator = 'Inflation'
GROUP BY country
ORDER BY latest_gdp DESC;