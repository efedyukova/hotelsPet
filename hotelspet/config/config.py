import os
from dotenv import dotenv_values
import json

ENV = os.getenv("TEST_ENV", "dev")

ENV_FILE = f"hotelspet/config/env.db.{ENV}"
if not os.path.exists(ENV_FILE):
    raise FileNotFoundError(f"Environment file {ENV_FILE} not found!")

ENV_VARS = dotenv_values(ENV_FILE)

if "BASE_URL" not in ENV_VARS or "BOOKING_PAYLOAD" not in ENV_VARS:
    raise KeyError("Missing required environment variables in the environment file!")

BASE_URL = ENV_VARS["BASE_URL"]
BOOKING_ENDPOINT = ENV_VARS["BOOKING_ENDPOINT"]

BOOKING_PAYLOAD = json.loads(ENV_VARS["BOOKING_PAYLOAD"])
