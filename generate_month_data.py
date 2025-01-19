import numpy as np
import pandas as pd
import argparse
from datetime import datetime, timedelta
import random
from enum import Enum

from main import malls_data
from models import AgeRange, Gender

# Configuration for peak hours and visit durations
peak_hours = {"midday": 12, "evening": 18}
avg_durations_s = {"short": 5 * 60, "long": 20 * 60}

# Helper function to generate visitor count
def generate_visitors_count(peak_hour):
    """
    Generate visitors count using a Poisson distribution.
    """
    return np.random.poisson(20 if peak_hour else 5)

# Helper function to generate visit duration
def generate_duration(average_duration):
    """
    Generate visit duration using a Gaussian distribution.
    """
    return max(1, int(np.random.normal(average_duration, average_duration * 0.3)))

# Helper function to generate the start and end dates for the month
def get_start_end_date(month: int, year: int):
    """
    Generate start and end dates for the specified month and year.
    """
    start_date = datetime(year, month, 1, 8, 0)
    if month == 12:
        end_date = datetime(year + 1, 1, 1, 22, 0) - timedelta(hours=1)
    else:
        end_date = datetime(year, month + 1, 1, 22, 0) - timedelta(hours=1)
    return start_date, end_date

# Function to generate traffic data
def generate_traffic_data(year: int, month: int, output_path: str):
    """
    Generate traffic data for the entire month and save to a CSV file.
    """
    # Get the start and end dates based on the month
    start_date, end_date = get_start_end_date(month, year)
    
    # Generate hourly timestamps between start and end date
    hours = pd.date_range(start=start_date, end=end_date, freq="H").to_pydatetime()

    # Generate traffic data
    traffic_data = []

    for mall_name, stores in malls_data.items():
        for store_name in stores:
            peak_hour_type = random.choice(["midday", "evening"])
            average_duration_type = random.choice(["short", "long"])

            for hour in hours:
                if 8 <= hour.hour <= 22:
                    peak_hour = abs(hour.hour - peak_hours[peak_hour_type]) < 2
                    visitors = generate_visitors_count(peak_hour)
                    avg_duration = generate_duration(avg_durations_s[average_duration_type])

                    for _ in range(visitors):
                        data_entry = {
                            "mall_name": mall_name,
                            "store_name": store_name,
                            "timestamp_hour": hour,
                            "gender": random.choice(list(Gender)),
                            "age_range": random.choice(list(AgeRange)),
                            "visitors": visitors,
                            "avg_duration_seconds": avg_duration,
                        }
                        traffic_data.append(data_entry)

    # Save to CSV
    df = pd.DataFrame(traffic_data)
    df.to_csv(output_path, index=False)
    print(f"Traffic data for {start_date.strftime('%B %Y')} has been generated and saved as '{output_path}'.")

# Main function to handle command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate traffic data for a given month and output path.")
    parser.add_argument("year", type=int, help="Year")
    parser.add_argument("month", type=int, choices=range(1, 13), help="Month of the year (1-12)")
    parser.add_argument("output_path", type=str, help="Path to save the generated CSV file")

    args = parser.parse_args()

    # Generate traffic data
    generate_traffic_data(args.year, args.month, args.output_path)

