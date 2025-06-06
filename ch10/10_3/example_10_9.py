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


Promotion = Callable[[Order], Decimal]

promos: list[Promotion] = []

def promotion(promo: Promotion) -> Promotion:
    promos.append(promo)
    return promo

def best_promo(order: Order) -> Decimal:
    return max(promo(order) for promo in promos)


@promotion
def fidelity(order: Order) -> Decimal:
    rate = Decimal('0.05')
    return order.total() * rate if order.customer.fidelity >= 1000 else Decimal(0)

@promotion
def bulk_item(order: Order) -> Decimal:
    return sum((item.total() * Decimal('0.1') for item in order.cart if item.quantity >= 20), start=Decimal(0))

@promotion
def large_order(order: Order) -> Decimal:
    distinct_items = {item.product for item in order.cart}
    return order.total() * Decimal('0.07') if len(distinct_items) >= 10 else Decimal(0)

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)

cart = (LineItem('banana', 4, Decimal('.5')), LineItem('apple', 10, Decimal('1.5')), LineItem('watermelon', 5, Decimal(5)))
banana_cart = (LineItem('banana', 30, Decimal('.5')), LineItem('apple', 10, Decimal('1.5')))
long_cart = tuple(LineItem(str(sku), 1, Decimal(1)) for sku in range(10))

print('*' * 40)
print(f'Order(joe, cart, fidelity): {Order(joe, cart, fidelity)}')
print(f'Order(joe, cart, bulk_item): {Order(joe, cart, bulk_item)}')
print(f'Order(joe, cart, large_order): {Order(joe, cart, large_order)}')
print(f'Order(joe, cart, best_promo): {Order(joe, cart, best_promo)}')
print('*' * 40)
print(f'Order(ann, cart, fidelity): {Order(ann, cart, fidelity)}')
print(f'Order(ann, cart, bulk_item): {Order(ann, cart, bulk_item)}')
print(f'Order(ann, cart, large_order): {Order(ann, cart, large_order)}')
print(f'Order(ann, cart, best_promo): {Order(ann, cart, best_promo)}')
print('*' * 40)
print(f'Order(joe, banana_cart, fidelity): {Order(joe, banana_cart, fidelity)}')
print(f'Order(joe, banana_cart, bulk_item): {Order(joe, banana_cart, bulk_item)}')
print(f'Order(joe, banana_cart, large_order): {Order(joe, banana_cart, large_order)}')
print(f'Order(joe, banana_cart, best_promo): {Order(joe, banana_cart, best_promo)}')
print('*' * 40)
print(f'Order(joe, long_cart, fidelity): {Order(joe, long_cart, fidelity)}')
print(f'Order(joe, long_cart, bulk_item): {Order(joe, long_cart, bulk_item)}')
print(f'Order(joe, long_cart, large_order): {Order(joe, long_cart, large_order)}')
print(f'Order(joe, long_cart, best_promo): {Order(joe, long_cart, best_promo)}')
