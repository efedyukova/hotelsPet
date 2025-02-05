import json
import os
from dotenv import dotenv_values

ENV = os.getenv("TEST_ENV", "dev")

with open(os.path.join(os.path.dirname(__file__), "environments.json")) as f:
    CONFIG = json.load(f)

ENV_FILE = os.path.join(os.path.dirname(__file__), CONFIG[ENV]["ENV_FILE"])
ENV_VARS = dotenv_values(ENV_FILE)

BASE_URL = ENV_VARS["BASE_URL"]
BOOKING_ENDPOINT = ENV_VARS["BOOKING_ENDPOINT"]
BOOKING_PAYLOAD = json.loads(ENV_VARS["BOOKING_PAYLOAD"])
