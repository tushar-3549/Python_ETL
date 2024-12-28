import pandas as pd

def extract(f):
    try:
        df = pd.read_csv(f)
        return df
    except Exception as e:
        print(f"Error extracting data : {e}")
        return None
