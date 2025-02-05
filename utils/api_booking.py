import requests
from config.config import BASE_URL, BOOKING_ENDPOINT
from utils.error_handler import error_handler


class APIClient:
    def __init__(self):
        self.base_url = BASE_URL

    def create_booking(self, payload):
        url = f"{self.base_url}{BOOKING_ENDPOINT}"
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            error_handler.log_error(f"API request failed: {e}")
            return None


api_client = APIClient()
