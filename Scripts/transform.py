import pandas as pd
from config import RAW_FILE, PROCESSED_FILE


def run_transformation():

    # Load raw extracted data
    df = pd.read_csv(
        RAW_FILE
    )

    # Remove missing values
    df = df.dropna(subset=["value"])

    # Convert data types
    df["year"] = df["year"].astype(int)

    df["value"] = df["value"].astype(float)

    # Sort values
    df = df.sort_values(
        by=["country", "indicator", "year"]
    )

    # Save cleaned data
    df.to_csv(
        PROCESSED_FILE,
        index=False
    )

    print("Transformation completed!")