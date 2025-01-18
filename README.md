# fake-mall-traffic-api


## Install
pip install fastapi uvicorn
pip install -r requirements.txt

## Run
uvicorn main:app --reload

## Test
curl -X POST http://127.0.0.1:8000/malls
curl -X POST "http://127.0.0.1:8000/malls-stores?mall_name=Centre%20Saint%20Martial"
curl -X POST "http://127.0.0.1:8000/mall-visits?mall_name=Centre%20Saint%20Martial&start_date_hour=2025-01-15T09:00:00&end_date_hour=2025-01-15T18:00:00"
