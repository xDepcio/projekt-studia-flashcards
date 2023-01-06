from card_collection import (
    CardCollection,
    CardCollectionEmpty,
    CardCollectionNotEnoughUnique
)
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


def test_card_collection_draw_unique_too_much():
    cc = CardCollection([
        Card(1, 'a', 'a'),
        Card(2, 'a', 'a'),
        Card(3, 'a', 'a')
    ], 'vehicles')
    with pytest.raises(CardCollectionNotEnoughUnique):
        cc.draw_cards(4)


def test_card_collection_draw_cards_unique():
    dummy_cards = [
        Card(1, 'a', 'a'),
        Card(2, 'a', 'a'),
        Card(3, 'a', 'a')
    ]
    cc = CardCollection(dummy_cards, 'vehicles')
    cards = cc.draw_cards(3)
    for card in cards:
        assert card in dummy_cards
