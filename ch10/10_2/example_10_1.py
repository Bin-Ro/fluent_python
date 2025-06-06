from abc import ABC, abstractmethod
from collections.abc import Sequence
from decimal import Decimal
from typing import NamedTuple, Optional

class Customer(NamedTuple):
    name: str
    fidelity: int

class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self) -> Decimal:
        return self.price * self.quantity

class Order(NamedTuple):
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional['Promotion'] = None

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))

    def due(self) -> Decimal:
        discount = Decimal(0) if self.promotion is None else self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'

class Promotion(ABC):
    @abstractmethod
    def discount(self, order: Order) -> Decimal:
        pass

class FidelityPromo(Promotion):
    def discount(self, order: Order) -> Decimal:
        rate = Decimal('0.05')
        return order.total() * rate if order.customer.fidelity >= 1000 else Decimal(0)

class BulkItemPromo(Promotion):
    def discount(self, order: Order) -> Decimal:
        return sum((item.total() * Decimal('0.1') for item in order.cart if item.quantity >= 20), start=Decimal(0))

class LargeOrderPromo(Promotion):
    def discount(self, order: Order) -> Decimal:
        distinct_items = {item.product for item in order.cart}
        return order.total() * Decimal('0.07') if len(distinct_items) >= 10 else Decimal(0)

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)

cart = (LineItem('banana', 4, Decimal('.5')), LineItem('apple', 10, Decimal('1.5')), LineItem('watermelon', 5, Decimal(5)))

print(Order(joe, cart, FidelityPromo()))
print(Order(ann, cart, FidelityPromo()))

banana_cart = (LineItem('banana', 30, Decimal('.5')), LineItem('apple', 10, Decimal('1.5')))

print(Order(joe, banana_cart, BulkItemPromo()))

long_cart = tuple(LineItem(str(sku), 1, Decimal(1)) for sku in range(10))

print(Order(joe, long_cart, LargeOrderPromo()))
print(Order(joe, cart, LargeOrderPromo()))
