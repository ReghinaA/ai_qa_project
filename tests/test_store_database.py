"""Test the connection to the local store database and its basic structure."""

import os
import sqlite3
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

def get_store_db_path() -> Path:
    configured_path = os.getenv("STORE_DB_PATH")

    assert configured_path, (
        "STORE_DB_PATH is not configured in .env"
    )

    database_path = Path(configured_path)

    assert database_path.exists(), (
        f"Store database was not found: {database_path}"
    )

    return database_path


def connect_to_store_read_only():
    database_path = get_store_db_path()
    database_uri = f"{database_path.as_uri()}?mode=ro"

    return sqlite3.connect(
        database_uri,
        uri=True,
    )


def test_store_database_contains_products_table():
    with connect_to_store_read_only() as connection:
        result = connection.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
              AND name = 'products'
            """
        ).fetchone()

    assert result == ("products",)


def test_store_contains_products():
    with connect_to_store_read_only() as connection:
        product_count = connection.execute(
            "SELECT COUNT(*) FROM products"
        ).fetchone()[0]

    assert product_count > 0