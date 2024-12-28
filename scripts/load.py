import psycopg2

def load(data, **db_conf):
    try:
        conn = psycopg2.connect(**db_conf)
        cur = conn.cursor()

        # insert data row by row
        for _, row in data.iterrows():
            cur.execute("""
                INSERT INTO sales_data (order_id, product, quantity, price, total_price, date)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (row['OrderID'], row['Product'], row['Quantity'], row['Price'], row['Total_Price'], row['Date']))
        conn.commit()
        cur.close()
        conn.close()
        print("Data loaded successful.")
    except Exception as e:
        print(f"Error loading data: {e}")