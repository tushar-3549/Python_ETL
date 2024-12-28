## Database setup at postgreSQL DB:
```sql
CREATE DATABASE etl_demo;

CREATE TABLE sales_data (
    order_id SERIAL PRIMARY KEY,
    product VARCHAR(100),
    quantity INT,
    price FLOAT,
    total_price FLOAT,
    date DATE
);
```

## Run the ETL Process at VS Code terminal:
`python3 -m scripts.main`

