from random import choices


class CardCollectionEmpty(Exception):
    def __init__(self, title):
        super().__init__(title)


class CardCollection:
    def __init__(self, cards, category):
        self.cards = cards
        self.category = category

    def add_cards(self, cards):
        self.cards = [*self.cards, *cards]

    def remove_cards(self, cards):
        pass

    def draw_cards(self, amount, unique=True):
        if len(self.cards) <= 0:
            raise CardCollectionEmpty('Cannot draw from empty CardCollection')

        choosen_cards = []
        weights = [card.popularity for card in self.cards]

        while len(choosen_cards) < amount:
            card = choices(self.cards, weights=weights, k=1)[0]
            if unique and card not in choosen_cards:
                choosen_cards.append(card)
            elif not unique:
                choosen_cards.append(card)

        return choosen_cards