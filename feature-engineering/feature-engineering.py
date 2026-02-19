# feature engineering.py
import pandas as pd
import logging
from pathlib import Path

#configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Read the validated data from the specified path
def read_validated_data(file_path):
    logger.info(f"Reading validated data from {file_path}")
    df = pd.read_csv(file_path)
    logger.info(f"Validated data read successfully with shape {df.shape}")
    return df

# Perform feature engineering on the validated data
def perform_feature_engineering(df):
    logger.info("Performing feature engineering on the validated data")
    # Example feature engineering: creating a new feature 'total_price' by multiplying 'quantity' and 'price'
    if 'quantity' in df.columns and 'price' in df.columns:
        df['total_price'] = df['quantity'] * df['price']
        logger.info("Feature engineering successful: 'total_price' created")
    else:
        logger.warning("Required columns for feature engineering not found: 'quantity' and 'price'")
        raise ValueError("Required columns for feature engineering not found: 'quantity' and 'price'")
    return df

# Save the engineered features to a specified path
def save_engineered_features(df, output_path):
    logger.info(f"Saving engineered features to {output_path}")
    df.to_csv(output_path, index=False)
    logger.info("Engineered features saved successfully")

if __name__ == "__main__":
    input_file_path = "data/data.csv"
    output_file_path = "data/engineered_features.csv"

    try:
        # Step 1: Read the validated data
        validated_data = read_validated_data(input_file_path)

        # Step 2: Perform feature engineering
        engineered_data = perform_feature_engineering(validated_data)

        # Step 3: Save the engineered features
        save_engineered_features(engineered_data, output_file_path)

    except Exception as e:
        logger.error(f"An error occurred during feature engineering: {e}")