"""Tax calculation utilities for Globomantics checkout."""

from src.models.order import Order


# Add tax calculation to checkout
def calculate_tax(order: Order) -> float:
    ...
