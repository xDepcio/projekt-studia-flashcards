from card import Card
from card_collection import CardCollection
from utils import import_cards
from stats import Stats
from datetime import datetime
from time import time


def test_card_collection_draw_cards_unique():
    c1 = Card(1, 'fura1', 'car1', 'vehicles')
    c2 = Card(2, 'fura2', 'car2', 'vehicles')
    c3 = Card(3, 'fura3', 'car3', 'vehicles')
    c4 = Card(4, 'fura4', 'car4', 'vehicles')
    c5 = Card(5, 'fura5', 'car5', 'vehicles')

    cc = CardCollection([c1, c2, c3, c4, c5], 'vehicles')
    cards = cc.draw_cards(5)
    for card in cards:
        assert card in [c1, c2, c3, c4, c5]


def test_import_cards():
    cards = import_cards('test2.json')
    assert cards[0].id == 1
    assert cards[0].origin_lang_value == 'Ciężarówka'
    assert cards[0].learning_lang_value == 'Truck'
    assert cards[0].category == 'Vehicles'


def test_stats_load():
    stats = Stats('stats.json')
    stats.load_stats()
    print(stats.data)


def test_stats_save():
    date = datetime.fromtimestamp(time())
    date = f'{date.year}-{date.month}-{date.day} {date.hour}:{date.minute}'

    stats = Stats('stats.json')
    stats.load_stats()
    stats.data['answers']['totalCorrect'] += 1
    stats.data['answers']['correct'].append({
        "originLang": 'fura prez ó',
        "learningLang": 'ride',
        "date": date
    })
    print(stats.data)
    stats.save_stats()


# test_stats_save()
