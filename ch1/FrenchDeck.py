import collections
import random

Card = collections.namedtuple('Card', 'rank suit')

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, card):
        self._cards[position] = card

    def __iter__(self):
        return iter(self._cards)

    def __repr__(self):
        return '\n'.join(map(repr, self._cards))

    def __contains__(self, card):
        return card in self._cards


deck = FrenchDeck()
print(f'len(deck): {len(deck)}')

print(f'deck[0]: {deck[0]}')
print(f'deck[-1]: {deck[-1]}')

print(deck, '\n')

random.shuffle(deck)
for card in deck:
    print(card)

print(f"Card('Q', 'hearts') in deck: {Card('Q', 'hearts') in deck}")
print(f"Card('7', 'bearts') in deck: {Card('7', 'bearts') in deck}")

deck = FrenchDeck()
for card in reversed(deck):
    print(card)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

print('\nsorted deck:\n')
for card in sorted(deck, key=spades_high):
    print(card)
