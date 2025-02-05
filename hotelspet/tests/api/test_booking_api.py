import allure
import pytest
from hotelspet.utils.api_booking import api_client
from hotelspet.config.config import BOOKING_PAYLOAD
from hotelspet.utils.error_handler import error_handler


@allure.feature("Booking API")
@allure.story("Create Booking")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
def test_create_booking():
    """Test creating a new booking"""
    with allure.step("Send API request to create booking"):
        response = api_client.create_booking(BOOKING_PAYLOAD)

    with allure.step("Validate response status code"):
        assert response is not None, "API request failed"
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    with allure.step("Validate response contains booking ID"):
        response_json = response.json()
        assert "bookingid" in response_json, "Response does not contain bookingid"

    error_handler.log_info("✅ API test passed successfully!")

if __name__ == "__main__":
    test_create_booking()
    print("✅ API test completed!")
