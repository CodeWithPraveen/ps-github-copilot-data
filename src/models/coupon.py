from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum


class DiscountType(str, Enum):
    PERCENTAGE = "percentage"
    FIXED = "fixed"


@dataclass
class Coupon:
    code: str
    discount_type: DiscountType
    value: float
    expires_at: datetime

    def is_valid(self, now: datetime | None = None) -> bool:
        now = now or datetime.now(timezone.utc)
        return now < self.expires_at


class CouponExpiredError(Exception):
    pass


class CouponNotFoundError(Exception):
    pass
