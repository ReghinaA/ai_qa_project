"""Test read-only product retrieval from the local store database."""

from src.store_repository import find_product_by_name

def test_find_existing_product():
    product = find_product_by_name("Men's Polo")

    assert product is not None
    assert product.product_id == 1
    assert product.name == "Men's Polo"
    assert product.price == 9.99
    assert product.stock == 2


def test_product_search_is_case_insensitive():
    product = find_product_by_name("men's polo")

    assert product is not None
    assert product.name == "Men's Polo"


def test_nonexistent_product_returns_none():
    product = find_product_by_name(
        "Product that does not exist"
    )

    assert product is None