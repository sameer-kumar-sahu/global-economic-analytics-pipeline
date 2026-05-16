from extract import run_extraction
from transform import run_transformation
from forecast import run_forecast
from load import run_load
from logger_config import setup_logger


logger = setup_logger()


def run_pipeline():

    try:
        logger.info("ETL Pipeline Started")

        print("Starting Extraction...")
        run_extraction()
        logger.info("Extraction Completed")

        print("Starting Transformation...")
        run_transformation()
        logger.info("Transformation Completed")

        print("Starting Forecasting...")
        run_forecast()
        logger.info("Forecasting Completed")

        print("Starting Load...")
        run_load()
        logger.info("Load Completed")

        logger.info("ETL Pipeline Completed Successfully")
        print("\nETL Pipeline Completed Successfully!")

    except Exception as e:
        logger.error(f"Pipeline Failed: {e}")
        print("\nPipeline Failed")
        print(e)


if __name__ == "__main__":
    run_pipeline()