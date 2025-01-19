import duckdb
import os


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


# Load all files into duckdb
def load_files_into_duckdb():
    load_data_into_duckdb("./data/2023_01.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2023_03.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2023_05.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2023_07.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2023_09.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2023_11.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2024_01.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2024_03.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2024_05.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2024_07.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2024_09.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2024_11.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2023_02.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2023_04.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2023_06.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2023_08.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2023_10.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2023_12.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2024_02.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2024_04.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2024_06.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2024_08.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2024_10.csv", "./duckdb/traffic_data.duckdb")
    load_data_into_duckdb("./data/2024_12.csv", "./duckdb/traffic_data.duckdb")


