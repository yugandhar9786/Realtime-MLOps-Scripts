import pandas as pd
import logging
from pathlib import Path

#configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Read the data from the specified path
def read_data(file_path):
    logger.info(f"Reading data from {file_path}")
    df = pd.read_csv(file_path)
    logger.info(f"Data read successfully with shape {df.shape}")
    return df

#validate the data for missing values and duplicates
def validate_data(df):
    logger.info("validating data for missing values and duplicates")
    if df.empty:
        logger.warning("Dataframe is empty")
        raise ValueError("Dataframe is empty")
    if df.isnull().sum().sum() > 0: 
        logger.warning("Dataframe contains missing values")
        raise ValueError("Dataframe contains missing values")
    if df.duplicated().sum() > 0:
        logger.warning("Dataframe contains duplicate values")
        raise ValueError("Dataframe contains duplicate values")
    logger.info("Data validation successful")

# Save the validated data to a specified path
def save_data(df, output_path):
    logger.info(f"Saving validated data to {output_path}")
    df.to_csv(output_path, index=False)
    logger.info("Data saved successfully")

if __name__ == "__main__":
    input_file_path = "data/raw/data.csv"
    output_file_path = "data/processed/validated_data.csv"

    try:
        # Step 1: Read the data
        data = read_data(input_file_path)

        # Step 2: Validate the data
        validate_data(data)

        # Step 3: Save the validated data
        save_data(data, output_file_path)

    except Exception as e:
        logger.error(f"An error occurred during data ingestion: {e}")
                
