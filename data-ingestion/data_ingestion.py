import pandas as pd
import logging
from pathlib import Path
# Configure logging
logging.basicConfig(level= logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
# Read function to read data from a CSV file
def read_data(file_path):
    logger.info(f"Reading data from {file_path}")
    df = pd.read_csv(file_path)
    return df
# Write validation function to check if the data is valid
def validate_data(df):
    logger.info("validating data")
    if df.empty:
        logger.warning("dataframe is empty")
        raise ValueError("Dataframe is empty")
    if "age" not in df.columns:
        raise ValueError("Missing 'age' column")
    logger.info("data validation successful")

# write save function to save the validated data to a new CSV file
def save_data(df, output_path):
    logger.info(f"saving data to {output_path}")
    df.to_csv(output_path, index=False)
    logger.info("data saved successfully")

if __name__ == "__main__":
    input_file = Path("data/sample.csv")
    output_file = Path("data/validated_sample.csv")
    df = read_data(input_file)
    validate_data(df)
    save_data(df, output_file)
