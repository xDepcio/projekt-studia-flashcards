from utils import (
    extend_cards_storage_from_json,
    import_cards,
    export_cards_to_json,
    get_categorized_cards_collections,
    add_card
)
from card import Card
import os
import json


def test_utils_extend_cards_storage_from_json():
    extend_cards_storage_from_json('cards.json', 'storage/cards.json')


def test_import_cards():
    cards = import_cards('tests/demo_cards.json')
    assert cards[0].id == 1
    assert cards[0].origin_lang_value == 'Ciężarówka'
    assert cards[0].learning_lang_value == 'Truck'
    assert cards[0].categories == ['Vehicles']
    assert cards[0].popularity == 0.3


def test_export_cards_to_json():
    cards = [
        Card(1, 'a', '_a', ['Vehicles'], 0.5),
        Card(2, 'a', '_a', ['Vehicles', 'Sports'], 0.2),
        Card(3, 'aź', '_aż'),
        Card(4, 'a', '_a'),
    ]
    if os.path.exists('tests/test_export.json'):
        os.remove('tests/test_export.json')
    export_cards_to_json('tests/test_export.json', cards)
    cards = json.load(open('tests/test_export.json', 'r', encoding='utf-8'))
    assert len(cards) == 4
    assert cards[0]['categories'] == ['Vehicles']
    assert cards[0]['popularity'] == 0.5
    assert cards[1]['categories'] == ['Vehicles', 'Sports']
    assert cards[1]['popularity'] == 0.2
    assert cards[2]['originLang'] == 'aź'
    assert cards[2]['learningLang'] == '_aż'
    assert cards[2]['popularity'] == 0.1
    assert cards[2]['categories'] == []


def test_get_categorized_cards_collections():
    c1 = Card(1, 'a', '_a', ['Vehicles'], 0.5)
    c2 = Card(2, 'a', '_a', ['Vehicles', 'Sports'], 0.2)
    c3 = Card(3, 'a', '_a')
    c4 = Card(4, 'a', '_a')

    cards = [c1, c2, c3, c4]

    cc_arr = get_categorized_cards_collections(cards)
    assert len(cc_arr) == 3
    for cc in cc_arr:
        assert cc.category in ['Wszystkie', 'Vehicles', 'Sports']
        for card in cc.cards:
            if cc.category == 'Wszystkie':
                assert card in cards
            elif cc.category == 'Vehicles':
                assert card in [c1, c2]
            elif cc.category == 'Sports':
                assert card in [c2]
