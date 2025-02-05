# **QA Automation Pet Project 🚀**

This is a **QA Automation Pet Project** that demonstrates **REST API testing** using **Python, Poetry, Pytest, and Allure**.  

## **📌 Features**
✔ **REST API tests** using `requests` and `pytest`  
✔ **Environment configuration** using `dotenv` (`env.db.dev`)  
✔ **Error handling** with structured logging  
✔ **Allure reporting** for better test visibility  
✔ **Poetry package management** for clean dependency handling  

---

## **🛠️ Project Structure**
```
/tests
    /api
        test_create_booking.py
/config
    config.py
    environments.json
    env.db.dev
/utils
    api_client.py
    error_handler.py
/reports
pyproject.toml
README.md
```

---

## **⚙️ Installation and Setup**
### **1. Install Poetry (if not installed)**
```sh
curl -sSL https://install.python-poetry.org | python3 -
```
Check the installation:
```sh
poetry --version
```

---

### **2. Clone the Repository**
```sh
git clone https://github.com/your-username/qa-pet-project.git
cd qa-pet-project
```

---

### **3. Install Dependencies**
```sh
poetry install
```

---

### **4. Environment Configuration**
All environment variables are stored in `/config/environments.json`, and the values are in files like `env.db.dev`:

#### **Example: `config/env.db.dev`**
```ini
# API Base URL
BASE_URL=https://restful-booker.herokuapp.com

# Endpoints
BOOKING_ENDPOINT=/booking

# Default Test Payload (JSON format)
BOOKING_PAYLOAD={"firstname": "John", "lastname": "Doe", "totalprice": 150, "depositpaid": true, "bookingdates": {"checkin": "2025-02-10", "checkout": "2025-02-20"}, "additionalneeds": "Breakfast"}
```

By default, the environment is `dev`. You can change it using:
```sh
TEST_ENV=staging poetry run pytest tests/api/test_create_booking.py
```

---

## **📝 Running Tests**
### **1. Run API Tests (default: `dev`)**
```sh
poetry run pytest tests/api/test_create_booking.py --alluredir=reports/
```

### **2. Run Tests in `staging` or `prod`**
```sh
TEST_ENV=staging poetry run pytest tests/api/test_create_booking.py --alluredir=reports/
```

### **3. View Allure Report**
```sh
poetry run allure serve reports/
```

---

## **📜 Code Overview**
### **API Client (`utils/api_client.py`)**
```python
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
```

---

### **Test Case (`tests/api/test_create_booking.py`)**
```python
import allure
import pytest
from utils.api_client import api_client
from config.config import BOOKING_PAYLOAD
from utils.error_handler import error_handler

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
```

---

## **✅ Best Practices Used**
✔ **Page Object Model (POM) for UI tests (if added later)**  
✔ **KISS, DRY, and SOLID principles**  
✔ **Structured configuration files (`env.db.dev`, `environments.json`)**  
✔ **Custom error handling and logging**  
✔ **Allure reporting for better debugging**  

---

## **🛠️ Future Improvements**
- **CI/CD Integration (GitHub Actions)**
- **Dockerized environment for tests**
- **UI tests with `pytest + selene`**

---

## **📜 License**
This project is open-source and free to use.
