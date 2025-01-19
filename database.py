import duckdb
import os
from typing import Optional
from datetime import datetime


# Function to load data from CSV into DuckDB
def load_data_into_duckdb(csv_file: str, db_path: str):
    """
    Load data from a CSV file into DuckDB database.
    """
    con = duckdb.connect(db_path)  # Connect to the DuckDB database
    print(f"Loading data from {csv_file} into DuckDB...")

    # Create table and load the CSV file into the database
    con.execute(f"""
        CREATE TABLE IF NOT EXISTS traffic_data (
            mall_name VARCHAR,
            store_name VARCHAR,
            timestamp_hour TIMESTAMP,
            gender VARCHAR,
            age_range VARCHAR,
            visitors INTEGER,
            avg_duration_seconds INTEGER
        );
    """)

    # Load the CSV data into the DuckDB table
    con.execute(f"""
        COPY traffic_data FROM '{csv_file}' (FORMAT CSV, HEADER);
    """)

    con.close()
    print(f"Data from {csv_file} has been successfully loaded into DuckDB.")


# Helper function to query DuckDB for mall visits
def query_traffic_data_from_duckdb(mall_name: Optional[str], start_date_hour: datetime, end_date_hour: datetime):
    """
    Query the traffic data table in DuckDB for the provided mall name and date range.
    Returns the list of results.
    """
    # Connect to DuckDB
    cwd = os.getcwd()
    db_path = os.path.join(cwd, "duckdb", "traffic_data.duckdb")
    con = duckdb.connect(db_path)

    # Build the base SQL query
    sql_query = """
        SELECT mall_name, store_name, timestamp_hour, gender, age_range, visitors, avg_duration_seconds
        FROM traffic_data
        WHERE timestamp_hour BETWEEN ? AND ?
    """

    # Add condition for mall_name if specified
    if mall_name:
        sql_query += " AND mall_name = ?"

    # Execute the query with the provided parameters
    params = [start_date_hour, end_date_hour]
    if mall_name:
        params.append(mall_name)

    result = con.execute(sql_query, params).fetchall()

    con.close()

    # Convert the result to a list of dictionaries
    columns = ["mall_name", "store_name", "timestamp_hour", "gender", "age_range", "visitors", "avg_duration_seconds"]
    return [dict(zip(columns, row)) for row in result]


# Load all files into duckdb
def load_files_into_duckdb():
    cwd = os.getcwd()
    load_data_into_duckdb(os.path.join(cwd, "data/2023_01.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2023_03.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2023_05.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2023_07.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2023_09.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2023_11.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2024_01.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2024_03.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2024_05.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2024_07.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2024_09.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2024_11.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2023_02.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2023_04.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2023_06.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2023_08.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2023_10.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2023_12.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2024_02.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2024_04.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2024_06.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2024_08.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2024_10.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))
    load_data_into_duckdb(os.path.join(cwd, "data/2024_12.csv"), os.path.join(cwd, "duckdb/traffic_data.duckdb"))



