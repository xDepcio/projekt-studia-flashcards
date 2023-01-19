from random import choices
from typing import List


class CardCollectionEmpty(Exception):
    def __init__(self, title):
        super().__init__(title)


class CardCollectionNotEnoughUnique(Exception):
    def __init__(self, title):
        super().__init__(title)


class CardCollection:
    def __init__(self, cards, category: str):
        self.cards = cards
        self.category = category

    def add_cards(self, cards: List):
        """Appends Card() objects from cards array to CardCollection()"""
        self.cards = [*self.cards, *cards]

    def remove_card(self, card):
        """Removes Card() object from cards array"""
        self.cards.remove(card)

    def draw_cards(self, amount: int, unique=True):
        """Returns array of Card() objects choosen from CardCollection().
        Cards with higher `popularity` attribute are choosen more often."""
        if len(self.cards) <= 0:
            raise CardCollectionEmpty('Cannot draw from empty CardCollection')

        if unique and amount > len(self.cards):
            raise CardCollectionNotEnoughUnique(
                'Not enough cards to draw only uniques'
            )

        if amount <= 0 or type(amount) is not int:
            raise ValueError('Amount to draw must be positive int')

        choosen_cards = []
        weights = [card.popularity for card in self.cards]

        while len(choosen_cards) < amount:
            card = choices(self.cards, weights=weights, k=1)[0]
            if unique and card not in choosen_cards:
                choosen_cards.append(card)
            elif not unique:
                choosen_cards.append(card)

        return choosen_cards
