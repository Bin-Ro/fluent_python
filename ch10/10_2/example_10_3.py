from collections.abc import Sequence
from dataclasses import dataclass
from decimal import Decimal
from typing import NamedTuple, Optional, Callable

class Customer(NamedTuple):
    name: str
    fidelity: int

class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self) -> Decimal:
        return self.price * self.quantity

@dataclass(frozen=True)
class Order:
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Callable[['Order'], Decimal]] = None

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))

    def due(self) -> Decimal:
        discount = Decimal(0) if self.promotion is None else self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'


def fidelity_promo(order: Order) -> Decimal:
    rate = Decimal('0.05')
    return order.total() * rate if order.customer.fidelity >= 1000 else Decimal(0)

def bulk_item_promo(order: Order) -> Decimal:
    return sum((item.total() * Decimal('0.1') for item in order.cart if item.quantity >= 20), start=Decimal(0))

def large_order_promo(order: Order) -> Decimal:
    distinct_items = {item.product for item in order.cart}
    return order.total() * Decimal('0.07') if len(distinct_items) >= 10 else Decimal(0)

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)

cart = (LineItem('banana', 4, Decimal('.5')), LineItem('apple', 10, Decimal('1.5')), LineItem('watermelon', 5, Decimal(5)))

print(Order(joe, cart, fidelity_promo))
print(Order(ann, cart, fidelity_promo))

banana_cart = (LineItem('banana', 30, Decimal('.5')), LineItem('apple', 10, Decimal('1.5')))

print(Order(joe, banana_cart, bulk_item_promo))

long_cart = tuple(LineItem(str(sku), 1, Decimal(1)) for sku in range(10))

print(Order(joe, long_cart, large_order_promo))
print(Order(joe, cart, large_order_promo))
