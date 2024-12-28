import pandas as pd

def transform(data):
    # filter missing values
    data = data.dropna()
    # remove invalid rows (negative quantities)
    data = data[data['Quantity'] > 0]
    # add total price column
    data['Total_Price'] = data['Quantity']*data['Price']
    #convert date column to date time
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d', errors='coerce')

    return data
