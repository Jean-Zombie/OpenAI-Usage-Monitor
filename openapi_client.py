from datetime import datetime, timedelta
import os
import requests
from dotenv import load_dotenv

load_dotenv()

today = datetime.now().date()
today = datetime.now().date()
first_day_of_current_month = today.replace(day=1)
first_day_of_next_month = (first_day_of_current_month + timedelta(days=32)).replace(
    day=1
)

first_day_of_current_month_str = first_day_of_current_month.strftime("%Y-%m-%d")
first_day_of_next_month_str = first_day_of_next_month.strftime("%Y-%m-%d")

API_KEY = os.getenv("API_KEY")
API_BASE_URL = "https://api.openai.com/v1/organizations/"
API_USAGE_URL = f"https://api.openai.com/dashboard/billing/usage?end_date={first_day_of_next_month_str}&start_date={first_day_of_current_month_str}"


def fetch_openapi_usage_statistics():
    # Replace the following line with your actual API endpoint to fetch usage statistics
    usage_url = API_USAGE_URL
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.get(usage_url, headers=headers)

    if response.status_code == 200:
        # Parse the JSON response and extract the usage statistics
        # Replace the following line with the actual path to the usage statistics in the JSON response
        raw_usage_value = response.json()["total_usage"]
        dollars = raw_usage_value / 100
        dollars_rounded = round(dollars, 2)
        return dollars_rounded
    else:
        print(
            f"Error fetching OpenAPI usage statistics: {response.status_code} - {response.text}"
        )
        return None


fetch_openapi_usage_statistics()
