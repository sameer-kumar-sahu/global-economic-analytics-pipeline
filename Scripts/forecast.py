import pandas as pd
from sklearn.linear_model import LinearRegression
from config import PROCESSED_FILE, FORECAST_FILE


def run_forecast():
    df = pd.read_csv(PROCESSED_FILE)

    forecast_rows = []

    forecast_indicators = ["GDP", "Population"]

    for country in df["country"].unique():
        for indicator in forecast_indicators:

            temp = df[
                (df["country"] == country) &
                (df["indicator"] == indicator)
            ].copy()

            temp = temp.sort_values("year")

            if len(temp) < 10:
                continue

            X = temp[["year"]]
            y = temp["value"]

            model = LinearRegression()
            model.fit(X, y)

            last_year = temp["year"].max()
            future_years = list(range(last_year + 1, last_year + 6))

            for year in future_years:
                prediction = model.predict(pd.DataFrame({"year": [year]}))[0]

                forecast_rows.append({
                    "country": country,
                    "indicator": indicator,
                    "year": year,
                    "forecast_value": prediction,
                    "model_name": "Linear Regression"
                })

    forecast_df = pd.DataFrame(forecast_rows)

    forecast_df.to_csv(
        FORECAST_FILE,
        index=False
    )

    print("Forecasting completed!")