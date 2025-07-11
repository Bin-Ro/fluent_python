from functools import singledispatch
from collections import abc
import fractions
import decimal
import html
import numbers

@singledispatch
def htmlize(obj: object) -> str:
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'

@htmlize.register
def _(text: str) -> str:
    content = html.escape(text).replace('\n', '<br/>\n')
    return f'<p>{content}</p>'

@htmlize.register
def _(seq: abc.Sequence) -> str:
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n<ul>'

@htmlize.register
def _(n: numbers.Integral) -> str:
    return f'<pre>{n} (0x{n:x})</pre>'

@htmlize.register
def _(n: bool) -> str:
    return f'<pre>{n}</pre>'

@htmlize.register(fractions.Fraction)
def _(x) -> str:
    frac = fractions.Fraction(x)
    return f'<pre>{frac.numerator}/{frac.denominator}</pre>'

@htmlize.register(decimal.Decimal)
@htmlize.register(float)
def _(x) -> str:
    frac = fractions.Fraction(x).limit_denominator()
    return f'<pre>{x} ({frac.numerator}/{frac.denominator})</pre>'

print(f'{"*" * 40}\nhtmlize({1, 2, 3}):\n{htmlize({1, 2, 3})}')
print(f'{"*" * 40}\nhtmlize(abs):\n{htmlize(abs)}')
print(f'{"*" * 40}\nhtmlize(42):\n{htmlize(42)}')
print(f'{"*" * 40}\nhtmlize(["alpha", 66, {3, 2, 1}]):\n{htmlize(["alpha", 66, {3, 2, 1}])}')
print(f'{"*" * 40}\nhtmlize(True):\n{htmlize(True)}')
print(f'{"*" * 40}\nhtmlize(fractions.Fraction(2, 3)):\n{htmlize(fractions.Fraction(2, 3))}')
print(f'{"*" * 40}\nhtmlize(2/3):\n{htmlize(2/3)}')
print(f'{"*" * 40}\nhtmlize(decimal.Decimal("0.02380952")):\n{htmlize(decimal.Decimal("0.02380952"))}')
