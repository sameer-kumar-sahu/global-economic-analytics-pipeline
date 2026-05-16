import requests
import pandas as pd
from config import COUNTRIES, INDICATORS, RAW_FILE


def fetch_world_bank_data(country_code, indicator_code, indicator_name):

    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}?format=json&per_page=100"

    response = requests.get(url)

    data = response.json()

    records = data[1]

    cleaned_data = []

    for item in records:

        cleaned_data.append({
            "country": item["country"]["value"],
            "country_code": country_code,
            "indicator": indicator_name,
            "year": item["date"],
            "value": item["value"]
        })

    return pd.DataFrame(cleaned_data)


def run_extraction():


    all_dataframes = []

    for country_code, country_name in COUNTRIES.items():
        
        for indicator_code, indicator_name in INDICATORS:

            print(f"Fetching {indicator_name} data for {country_name}")

            df = fetch_world_bank_data(
                country_code,
                indicator_code,
                indicator_name
            )

            all_dataframes.append(df)

    combined_df = pd.concat(
        all_dataframes,
        ignore_index=True
    )

    combined_df.to_csv(
        RAW_FILE,
        index=False
    )

    print("\nGlobal extraction completed!")