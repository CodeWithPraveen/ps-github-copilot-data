from src.models.coupon import Coupon
from src.models.order import Order

COUPONS: dict[str, Coupon] = {}


def apply_coupon(order: Order, coupon_code: str) -> Order:
    """Apply a coupon to the given order and return the updated order."""
