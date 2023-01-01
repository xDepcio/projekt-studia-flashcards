from card_collection import CardCollection, CardCollectionEmpty
from card import Card
import pytest


def test_card_collection_init():
    c1 = Card(1, 'samochód', 'card')
    c2 = Card(2, 'samochód', 'card')
    cc = CardCollection([c1, c2], 'Vehicles')
    assert cc.cards.index(c1) is not None
    assert cc.cards.index(c2) is not None
    assert cc.category == 'Vehicles'


def test_card_collection_draw_cards_empty():
    cc = CardCollection([], 'vehicles')
    with pytest.raises(CardCollectionEmpty):
        cc.draw_cards(1)
