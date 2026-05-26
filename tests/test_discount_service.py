import pytest
from src.models.coupon import Coupon, DiscountType
from src.models.customer import Customer
from src.models.order import Order, OrderItem
from src.services.discount_service import validate_coupon
