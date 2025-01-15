
# Enum for gender
from datetime import datetime
from enum import Enum

from pydantic import BaseModel


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

