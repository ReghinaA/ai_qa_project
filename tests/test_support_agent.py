"""Test deterministic Tier 1 customer support responses."""

from src.support_agent import get_product_price_response


def test_existing_product_returns_grounded_price_and_stock():
    """Return the database price and availability for an existing product."""
    response = get_product_price_response("Men's Polo")

    assert response == "Men's Polo costs $9.99 and is currently in stock."


def test_zero_stock_product_returns_out_of_stock():
    """Report a product with zero stock as out of stock."""
    response = get_product_price_response("Women's t-shirt 2")

    assert response == "Women's t-shirt 2 costs $5.99 and is currently out of stock."


def test_nonexistent_product_returns_not_found():
    """Return a safe response when the product does not exist."""
    response = get_product_price_response("Purple Flying Toaster")

    assert response == "Sorry, I couldn't find 'Purple Flying Toaster'."