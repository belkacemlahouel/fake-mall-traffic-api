from fastapi import FastAPI, HTTPException, Query
from typing import List, Dict, Optional
from datetime import datetime
from database import query_traffic_data_from_duckdb, load_files_into_duckdb

# FastAPI instance
app = FastAPI()
load_files_into_duckdb()

# In-memory data storage for simplicity
store_visits = []

# Predefined data for malls and stores around Limoges
malls_data = {
    "Centre Saint Martial": ["H&M", "Sephora", "Fnac", "Camaïeu"],
    "Family Village Limoges": ["Decathlon", "Kiabi", "Boulanger", "La Grande Récré"],
    "Ester Technopole Mall": ["Apple Store", "Samsung Experience", "Tech Hub", "Gadget World"],
    "Cora Limoges": ["Intermarché", "JouéClub", "Brico Dépôt", "Maisons du Monde"]
}

@app.post("/heartbeat")
def heartbeat():
    """
    Heartbeat endpoint to check if the application is running.
    Returns the current server timestamp.
    """
    return {"status": "alive", "timestamp": datetime.utcnow().isoformat()}

@app.post("/malls")
def get_malls():
    """
    Retrieve the list of predefined malls.
    """
    return list(malls_data.keys())

@app.post("/malls-stores")
def get_stores_in_mall(mall_name: str = Query(..., description="Name of the mall")):
    """
    Retrieve the list of stores in a specific mall.
    """
    if mall_name not in malls_data:
        raise HTTPException(status_code=404, detail=f"Mall '{mall_name}' not found")
    return malls_data[mall_name]

@app.post("/mall-visits")
def get_mall_all_store_visits(
    mall_name: Optional[str] = Query(None, description="Name of the mall"),
    start_date_hour: datetime = Query(..., description="Start timestamp in YYYY-MM-DDTHH format"),
    end_date_hour: datetime = Query(..., description="End timestamp in YYYY-MM-DDTHH format")
):
    """
    Retrieve store visit records within a given date range from DuckDB.
    Optionally filter by mall name.
    """
    VALID_START_DATE = datetime(2023, 1, 1)
    VALID_END_DATE = datetime.today()  # updated at each call on purpose

    # Check if the start_date_hour and end_date_hour are within valid bounds
    if start_date_hour < VALID_START_DATE or end_date_hour > VALID_END_DATE:
        raise HTTPException(
            status_code=400,
            detail=f"Date range must be between {VALID_START_DATE.strftime('%Y-%m-%d')} and {VALID_END_DATE.strftime('%Y-%m-%d')}"
        )

    # Ensure start_date_hour is before or equal to end_date_hour
    if start_date_hour > end_date_hour:
        raise HTTPException(
            status_code=400,
            detail="Start date cannot be after end date"
        )

    # Query the DuckDB database for the requested data
    try:
        store_visits = query_traffic_data_from_duckdb(mall_name, start_date_hour, end_date_hour)
        if not store_visits:
            raise HTTPException(status_code=404, detail="No data found for the given criteria")

        return store_visits

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while querying the database: {str(e)}")

