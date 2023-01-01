from utils import extend_cards_storage, import_cards


def test_utils_extend_cards_storage():
    extend_cards_storage('cards.json', 'storage/cards.json')


def test_import_cards():
    cards = import_cards('storage/cards.json')
    assert cards[0].id == 1
    assert cards[0].origin_lang_value == 'Ciężarówka'
    assert cards[0].learning_lang_value == 'Truck'
    assert 'Vehicles' in cards[0].categories
