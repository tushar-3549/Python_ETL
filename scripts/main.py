from scripts.extract import extract
# from .extract import extract
from scripts.transform import transform
# from .transform import transform
from scripts.load import load
# from .load import load
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': os.getenv('DB_PORT', 5432)
}

file = './data/sales_data.csv'
# file = 'sales_data.csv'

if __name__ == "__main__":
    print("Starting ETL process...")
    
    # Extract
    print("Extracting data...")
    raw_data = extract(file)
    
    if raw_data is not None:
        # Transform
        print("Transforming data...")
        clean_data = transform(raw_data)
        
        # Load
        print("Loading data into database...")
        load(clean_data, **DB_CONFIG)
    
    print("ETL process completed.")