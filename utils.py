import json
from card import Card
from card_collection import CardCollection
from config import Config as cfg


def import_cards(path):
    """Reads list of cards from .json file at path formatted as:
    {
        "id": id, // int
        "originLang": originLang, // string
        "learningLang": learningLang, // string
        "categories": categories_arr, // strings array - optional
        "popularity": popularity // int (0.01 to 0.99)- optional
    }
    and returns array of Card() objects created from this list"""
    file = open(path, encoding='utf-8')
    imported_cards = json.load(file)
    cards = [
        Card(
            card['id'],
            card['originLang'],
            card['learningLang'],
            card.get('categories', None),
            card.get('popularity', None),
        )
        for card in imported_cards
    ]
    return cards


def extend_cards_storage(from_file, dest_file):
    """Reads list of cards from .json file at from_file path formatted as:
    {
        "originLang": originLang, // string
        "learningLang": learningLang, // string
        "categories": categories_arr, // strings array - optional
    }
    and saves only new ones to file at dest_file path"""
    file_new = open(from_file, encoding='utf-8')
    new_cards = json.load(file_new)
    file_old = open(dest_file, encoding='utf-8')
    old_cards = json.load(file_old)

    unique_words = set()
    cards = []

    id = 1
    for card in [*old_cards, *new_cards]:
        if card['originLang'].lower() not in unique_words:
            unique_words.add(card['originLang'].lower())
            card['id'] = id
            cards.append(card)
            id += 1

    with open(dest_file, 'w', encoding='utf-8') as fh:
        json.dump(cards, fh, indent=4, ensure_ascii=False)


def export_cards(destination_file_name, cards):
    """Saves Card() objects from cards array to file at
    destination_file_name path"""
    file = open(destination_file_name, 'x')
    data = []
    for card in cards:
        card_data = {
            'id': card.id,
            'originLang': card.origin_lang_value,
            'learningLang': card.learning_lang_value,
            'categories': card.categories,
            'popularity': card.popularity,
        }
        data.append(card_data)
    json.dump(data, file, indent=4, ensure_ascii=False)


def get_categorized_cards_collections(cards):
    """Returns array of CardCollection() objects where each collection
    contains cards of only certain category.
    One collection contains all cards"""
    categories_map = {'Wszystkie': CardCollection([], 'Wszystkie')}
    for card in cards:
        categories_map['Wszystkie'].add_cards([card])
        for category in card.categories:
            if category not in categories_map:
                categories_map[category] = CardCollection([card], category)
            else:
                categories_map[category].add_cards([card])
    return list(categories_map.values())


def add_card(origin_name, learn_name, categories=None, popularity=None):
    """Adds card with given arguments to file
    at path in CARDS_PATH env variable"""
    with open('temp_cards.json', 'w') as fh:
        card_data = {
            'originLang': origin_name,
            'learningLang': learn_name,
        }
        if categories is not None:
            card_data['categories'] = [categories]
        if popularity is not None:
            card_data['popularity'] = popularity

        json.dump([card_data], fh, indent=4, ensure_ascii=False)

    extend_cards_storage('temp_cards.json', cfg.CARDS_PATH)


def remove_card(card_obj):
    """Removes card associated to given Card() object from database in
    file at path CARDS_PATH env variable"""
    id = card_obj.id

    with open(cfg.CARDS_PATH, 'r') as fh:
        cards = json.load(fh)

    for card in cards:
        if card['id'] == id:
            cards.remove(card)
            break

    with open(cfg.CARDS_PATH, 'w') as fh:
        json.dump(cards, fh, indent=4, ensure_ascii=False)
