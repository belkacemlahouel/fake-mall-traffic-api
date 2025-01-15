from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Dict, Optional
from datetime import datetime

# Enum for gender
class Gender(str, Enum):
    male = "male"
    female = "female"
    unknown = "unknown"

# Enum for age range
class AgeRange(str, Enum):
    range_0_15 = "0-15"
    range_15_30 = "15-30"
    range_30_60 = "30-60"
    range_60_plus = "60+"

# Pydantic model for TrafficData
class TrafficData(BaseModel):
    mall_name: str
    timestamp_hour: datetime
    store_name: str
    gender: Gender
    age_range: AgeRange
    visitors: int
    avg_duration_seconds: int

# FastAPI instance
app = FastAPI()

# In-memory data storage for simplicity
store_visits = []

# Predefined data for malls and stores around Limoges
malls_data = {
    "Centre Saint Martial": ["H&M", "Sephora", "Fnac", "Camaïeu"],
    "Family Village Limoges": ["Decathlon", "Kiabi", "Boulanger", "La Grande Récré"],
    "Ester Technopole Mall": ["Apple Store", "Samsung Experience", "Tech Hub", "Gadget World"],
    "Cora Limoges": ["Intermarché", "JouéClub", "Brico Dépôt", "Maisons du Monde"]
}

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
    Retrieve store visit records within a given date range.
    Optionally filter by mall name.
    """
    filtered_visits = [
        visit for visit in store_visits
        if start_date_hour <= visit["timestamp_hour"] <= end_date_hour
        and (mall_name is None or visit["mall_name"] == mall_name)
    ]

    return filtered_visits

