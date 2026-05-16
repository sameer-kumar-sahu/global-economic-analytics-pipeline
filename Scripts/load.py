import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os


def run_load():

    load_dotenv()

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))

    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    engine = create_engine(DATABASE_URL)

    # Load cleaned CSV
    df = pd.read_csv("data/processed/global_economic_data_cleaned.csv")

    print("Main rows:", len(df))

    # Load flat table
    df.to_sql(
        name="economic_data",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("economic_data loaded!")

    # Reset star schema tables safely
    with engine.begin() as connection:

        connection.execute(text("SET FOREIGN_KEY_CHECKS = 0"))

        connection.execute(text("TRUNCATE TABLE fact_economic_data"))
        connection.execute(text("TRUNCATE TABLE dim_country"))
        connection.execute(text("TRUNCATE TABLE dim_indicator"))

        connection.execute(text("SET FOREIGN_KEY_CHECKS = 1"))

    print("Star schema tables cleared!")

    # Load dim_country using SQL, not pandas to_sql
    with engine.begin() as connection:

        connection.execute(text("""
            INSERT INTO dim_country
            (country_name, country_code)
            SELECT DISTINCT
                country,
                country_code
            FROM economic_data
        """))

    print("dim_country loaded!")

    # Load dim_indicator using SQL, not pandas to_sql
    with engine.begin() as connection:

        connection.execute(text("""
            INSERT INTO dim_indicator
            (indicator_name)
            SELECT DISTINCT
                indicator
            FROM economic_data
        """))

    print("dim_indicator loaded!")

    # Load fact_economic_data
    with engine.begin() as connection:

        connection.execute(text("""
            INSERT INTO fact_economic_data
            (country_id, indicator_id, year, value)
            SELECT
                c.country_id,
                i.indicator_id,
                e.year,
                e.value
            FROM economic_data e
            JOIN dim_country c
                ON e.country_code = c.country_code
            JOIN dim_indicator i
                ON e.indicator = i.indicator_name
        """))

    print("fact_economic_data loaded!")

    # Load forecast table
    forecast_df = pd.read_csv("data/processed/economic_forecast.csv")

    print("Forecast rows:", len(forecast_df))

    forecast_df.to_sql(
        name="economic_forecast",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("economic_forecast loaded!")

    print("\nLoad completed successfully!")


if __name__ == "__main__":
    run_load()