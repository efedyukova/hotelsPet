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
git clone https://github.com/your-username/hotels
cd hotels
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
TEST_ENV=staging poetry run pytest tests/api/test_booking_api.py
```

---

## **📝 Running Tests**
### **1. Run API Tests (default: `dev`)**
```sh
poetry run pytest hotelspet/tests/api/test_booking_api.py --alluredir=reports/
```

### **2. View Allure Report**
```sh
poetry run allure serve reports/
```

---

## **✅ Best Practices Used**
✔ **Page Object Model (POM) for UI tests (if added later)**  
✔ **KISS, DRY, and SOLID principles**  
✔ **Structured configuration files (`env.db.dev`, `environments.json`)**  
✔ **Custom error handling and logging**  
✔ **Allure reporting**  

---

## **📜 License**
This project is open-source and free to use.
