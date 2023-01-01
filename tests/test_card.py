from card import Card
import pytest
from utils import import_cards
from config import Config


def test_card_init_empty():
    with pytest.raises(TypeError):
        Card()


def test_card_init_bare_min():
    c = Card(1, 'samochód', 'car')
    assert c.id == 1
    assert c.origin_lang_value == 'samochód'
    assert c.learning_lang_value == 'car'
    assert c.popularity == 0.1
    assert c.categories == []


def test_card_evaluate_answer():
    c = Card(1, 'samochód', 'car')
    assert c.evaluate_answer('samochód') is True
    assert c.evaluate_answer('car') is False
    assert c.evaluate_answer('fdsfsd') is False


def test_card_handle_answer():
    c1 = Card(1, 'samochód', 'car')
    c1._handle_answer(True)
    c2 = Card(2, 'samochód', 'car')
    c2._handle_answer(False)
    c3 = Card(3, 'samochód', 'car')
    c3.popularity = 0.011
    c3._handle_answer(True)
    c4 = Card(4, 'samochód', 'car')
    c4.popularity = 0.98
    c4._handle_answer(False)
    assert c1.popularity == 0.1 * 0.75
    assert c2.popularity == 0.1 * 1.8
    assert c3.popularity == 0.01
    assert c4.popularity == 0.99


def test_card_save():
    card1 = import_cards(Config.CARDS_PATH)[0]
    pop = None
    if card1.popularity == 0.2:
        pop = 0.3
    else:
        pop = 0.2

    card1.popularity = pop
    card1._save()

    card2 = import_cards(Config.CARDS_PATH)[0]
    assert card2.popularity == pop
