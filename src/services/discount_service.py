from src.models.coupon import Coupon
from src.models.order import Order

COUPONS: dict[str, Coupon] = {}


def validate_coupon(code: str, order: Order) -> bool:
    """Return True if the coupon code exists, is not expired, and applies to this order."""
