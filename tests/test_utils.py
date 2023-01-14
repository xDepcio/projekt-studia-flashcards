from utils import (
    extend_cards_storage_from_json,
    import_cards,
    export_cards_to_json,
    get_categorized_cards_collections,
    add_card,
    extend_cards_storage_from_csv
)
from card import Card
import os
import json
from config import Config as cfg


def test_utils_extend_cards_storage_from_json():
    start_data = [
            {
                "id": 1,
                "originLang": "Ciężarówka",
                "learningLang": "Truck",
                "categories": [
                    "Vehicles"
                ],
                "popularity": 0.3
            },
            {
                "id": 2,
                "originLang": "Samochód",
                "learningLang": "Car",
                "categories": [
                    "Vehicles"
                ],
                "popularity": 0.7
            }
        ]

    with open(
        'tests/dummy_data/test_dest_extend_cards.json',
        'w', encoding='utf-8'
    ) as fh:
        json.dump(start_data, fh, indent=4, ensure_ascii=False)

    extend_cards_storage_from_json(
        'tests/dummy_data/test_cards_extend_cards_from_json.json',
        'tests/dummy_data/test_dest_extend_cards.json'
    )

    with open(
        'tests/dummy_data/test_dest_extend_cards.json',
        'r', encoding='utf-8'
    ) as fh:
        data = json.load(fh)
        card1 = {
            "id": 3,
            "originLang": "koszykówka",
            "learningLang": "basketball",
            "categories": ["Sports"],
        }
        assert card1 in data
        card2 = {
            "id": 4,
            "originLang": "noga",
            "learningLang": "football",
        }
        assert card2 in data


def test_utils_extend_cards_storage_from_csv():
    start_data = [
            {
                "id": 1,
                "originLang": "Ciężarówka",
                "learningLang": "Truck",
                "categories": [
                    "Vehicles"
                ],
                "popularity": 0.3
            },
            {
                "id": 2,
                "originLang": "Samochód",
                "learningLang": "Car",
                "categories": [
                    "Vehicles"
                ],
                "popularity": 0.7
            }
        ]

    with open(
        'tests/dummy_data/test_dest_extend_cards.json',
        'w', encoding='utf-8'
    ) as fh:
        json.dump(start_data, fh, indent=4, ensure_ascii=False)

    extend_cards_storage_from_csv(
        'tests/dummy_data/test_cards_extend_cards_from_csv.txt',
        'tests/dummy_data/test_dest_extend_cards.json'
    )

    with open(
        'tests/dummy_data/test_dest_extend_cards.json',
        'r', encoding='utf-8'
    ) as fh:
        data = json.load(fh)
        card1 = {
            "id": 3,
            "originLang": "koszykówka",
            "learningLang": "basketball",
            "categories": ["Sports"],
            "popularity": 0.1,
        }
        assert card1 in data
        card2 = {
            "id": 4,
            "originLang": "noga",
            "learningLang": "football",
            "categories": [],
            "popularity": 0.1,
        }
        assert card2 in data


def test_import_cards():
    cards = import_cards('tests/dummy_data/demo_cards.json')
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
    if os.path.exists('tests/dummy_data/test_export.json'):
        os.remove('tests/dummy_data/test_export.json')
    export_cards_to_json('tests/dummy_data/test_export.json', cards)
    cards = json.load(
        open('tests/dummy_data/test_export.json', 'r', encoding='utf-8'))
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


def test_add_card():
    origin_name = 'a'
    learn_name = '_a'
    categories = ['Vehicles']
    path = 'tests/dummy_data/test_add_card.json'

    with open(path, 'w', encoding='utf-8') as fh:
        json.dump([{
            "id": 1,
            "originLang": "Ciężarówka",
            "learningLang": "Truck",
            "categories": ["Vehicles"],
            "popularity": 0.3
        }], fh, indent=4, ensure_ascii=False)

    cfg.CARDS_PATH = path
    add_card(origin_name, learn_name, categories)

    with open(path, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
        assert {
            "originLang": "a",
            "learningLang": "_a",
            "categories": ["Vehicles"],
            "id": 2
        } in data
