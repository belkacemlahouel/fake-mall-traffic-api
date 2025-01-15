# fake-mall-traffic-api


## Install
pip install fastapi uvicorn

## Run
uvicorn main:app --reload

## Test
curl -X POST "http://127.0.0.1:8000/traffic" -H "Content-Type: application/json" -d '{"timestamp": "2025-01-15T12:00:00", "visitors": 200, "section": "Food Court"}'

curl -X POST "http://127.0.0.1:8000/store-visits/filter?start_date_hour=2025-01-15T10:00:00&end_date_hour=2025-01-15T15:00:00"

