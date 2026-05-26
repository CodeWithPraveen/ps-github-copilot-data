from datetime import datetime, timedelta, timezone

import pytest

from src.models.coupon import Coupon, CouponExpiredError, DiscountType
from src.models.customer import Customer
from src.models.order import Order, OrderItem
from src.services.checkout_service import COUPONS, apply_coupon


def _make_order() -> Order:
    customer = Customer(id="c1", email="a@b.com", locale="en_US", country_code="US")
    return Order(id="o1", customer=customer, items=[OrderItem("SKU-1", "Item", 2, 50.0)])


def test_apply_valid_percentage_coupon_sets_discount_amount():
    COUPONS["SAVE10"] = Coupon(
        code="SAVE10",
        discount_type=DiscountType.PERCENTAGE,
        value=10.0,
        expires_at=datetime.now(timezone.utc) + timedelta(days=1),
    )
    order = apply_coupon(_make_order(), "SAVE10")
    assert order.discount_amount == 10.0
    assert order.coupon_code == "SAVE10"


def test_apply_expired_coupon_raises():
    COUPONS["OLD"] = Coupon(
        code="OLD",
        discount_type=DiscountType.PERCENTAGE,
        value=10.0,
        expires_at=datetime.now(timezone.utc) - timedelta(days=1),
    )
    with pytest.raises(CouponExpiredError):
        apply_coupon(_make_order(), "OLD")
