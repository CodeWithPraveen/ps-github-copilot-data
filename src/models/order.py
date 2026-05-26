from dataclasses import dataclass, field
from typing import List, Optional

from src.models.customer import Customer


@dataclass
class OrderItem:
    sku: str
    name: str
    quantity: int
    unit_price: float


@dataclass
class Order:
    id: str
    customer: Customer
    items: List[OrderItem] = field(default_factory=list)
    discount_amount: float = 0.0
    coupon_code: Optional[str] = None

    @property
    def subtotal(self) -> float:
        return sum(item.quantity * item.unit_price for item in self.items)

    @property
    def total(self) -> float:
        return self.subtotal - self.discount_amount
