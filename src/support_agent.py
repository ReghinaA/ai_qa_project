"""Provide deterministic Tier 1 customer support responses."""

from src.store_repository import find_product_by_name


def get_product_price_response(product_name: str) -> str:
    """Return a concise grounded response with product price and availability."""
    product = find_product_by_name(product_name)

    if product is None:
        return f"Sorry, I couldn't find '{product_name}'."

    if product.stock > 0:
        availability = "currently in stock"
    else:
        availability = "currently out of stock"

    return (
        f"{product.name} costs ${product.price:.2f} "
        f"and is {availability}."
    )