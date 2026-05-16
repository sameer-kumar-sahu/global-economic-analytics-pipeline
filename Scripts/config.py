COUNTRIES = {
    "IN": "India",
    "US": "United States",
    "CN": "China",
    "DE": "Germany",
    "JP": "Japan"
}

INDICATORS = [
    ("NY.GDP.MKTP.CD", "GDP"),
    ("FP.CPI.TOTL.ZG", "Inflation"),
    ("SP.POP.TOTL", "Population")
]

RAW_FILE = "data/raw/global_economic_data.csv"
PROCESSED_FILE = "data/processed/global_economic_data_cleaned.csv"
FORECAST_FILE = "data/processed/economic_forecast.csv"

ECONOMIC_TABLE = "economic_data"
FORECAST_TABLE = "economic_forecast"