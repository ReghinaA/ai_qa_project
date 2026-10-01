"""Test the availability of the locally running e-commerce store."""

import os

import requests
from dotenv import load_dotenv


load_dotenv()

STORE_BASE_URL = os.getenv(
    "STORE_BASE_URL",
    "http://127.0.0.1:5000",
)


def test_store_is_available():
    response = requests.get(
        STORE_BASE_URL,
        timeout=5,
    )

    assert response.status_code == 200
    assert response.text