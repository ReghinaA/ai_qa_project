"""Provide safe read-only access to the local store database."""

import os
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

@dataclass(frozen=True)
class Product:
    product_id: int
    name: str
    price: float
    description: str
    stock: int


def get_store_db_path() -> Path:
    configured_path = os.getenv("STORE_DB_PATH")

    if not configured_path:
        raise RuntimeError(
            "STORE_DB_PATH is not configured in .env"
        )

    database_path = Path(configured_path)

    if not database_path.exists():
        raise FileNotFoundError(
            f"Store database was not found: {database_path}"
        )

    return database_path


def connect_to_store_read_only() -> sqlite3.Connection:
    database_path = get_store_db_path()
    database_uri = f"{database_path.as_uri()}?mode=ro"

    return sqlite3.connect(
        database_uri,
        uri=True,
    )


def find_product_by_name(name: str) -> Product | None:
    with connect_to_store_read_only() as connection:
        row = connection.execute(
            """
            SELECT
                productId,
                name,
                price,
                description,
                stock
            FROM products
            WHERE LOWER(name) = LOWER(?)
            LIMIT 1
            """,
            (name,),
        ).fetchone()

    if row is None:
        return None

    return Product(
        product_id=row[0],
        name=row[1],
        price=row[2],
        description=row[3],
        stock=row[4],
    )