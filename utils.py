import json
from card import Card
from card_collection import CardCollection
from config import Config as cfg
import csv
from typing import List
import ast
import os


def import_cards(path: str) -> List[Card]:
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


def extend_cards_storage_from_json(from_file: str, dest_file: str):
    """Reads list of cards from .json file at from_file path formatted as:
    {
        "originLang": originLang, // string
        "learningLang": learningLang, // string
        "categories": categories_arr, // strings array - optional
        "popularity": popularity // int (0.01 to 0.99)- optional
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


def extend_cards_storage_from_csv(from_file: str, dest_file: str):
    """Reads list of cards from .txt (csv) file
    at from_file path formatted as example:

    pokój,room,['Home'],0.1

    1st - origin lang value
    2nd - learning lang value
    3rd - categories array
    4th - popularity (0.01 to 0.99)
    and saves only new ones to file at dest_file path"""
    new_cards = []
    with open(from_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            originLang, learningLang, categories = row
            categories = ast.literal_eval(categories)
            new_cards.append({
                "originLang": originLang,
                "learningLang": learningLang,
                "categories": categories,
            })

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


def export_cards_to_json(destination_file_name: str, cards: List[Card]):
    """Saves Card() objects from cards array to .json file
    at destination_file_name path"""
    file = open(destination_file_name, 'w', encoding='utf-8')
    data = []
    for card in cards:
        card_data = {
            'originLang': card.origin_lang_value,
            'learningLang': card.learning_lang_value,
            'categories': card.categories,
        }
        data.append(card_data)
    json.dump(data, file, indent=4, ensure_ascii=False)


def export_cards_to_csv(dest_file_name: str, cards: List[Card]):
    """Saves Card() objects from cards array to .txt file
    at destination_file_name path"""
    with open(dest_file_name, 'w', encoding='utf-8', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for card in cards:
            originLang = card.origin_lang_value
            learningLang = card.learning_lang_value
            categories = card.categories
            csvwriter.writerow(
                [originLang, learningLang, categories]
            )


def get_categorized_cards_collections(
        cards: List[Card]) -> List[CardCollection]:
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


def add_card(
        origin_name: str, learn_name: str, categories: List[str] = None,
        popularity: float = None):
    """Adds card with given arguments to file
    at path in CARDS_PATH env variable"""
    path = 'temp_cards.json'
    with open(path, 'w', encoding='utf-8') as fh:
        card_data = {
            'originLang': origin_name,
            'learningLang': learn_name,
        }
        if categories is not None:
            card_data['categories'] = categories
        if popularity is not None:
            card_data['popularity'] = popularity

        json.dump([card_data], fh, indent=4, ensure_ascii=False)

    extend_cards_storage_from_json(path, cfg.CARDS_PATH)
    os.remove(path)


def remove_card(card_obj: Card):
    """Removes card associated to given Card() object from database in
    file at path CARDS_PATH env variable"""
    id = card_obj.id

    with open(cfg.CARDS_PATH, 'r', encoding='utf-8') as fh:
        cards = json.load(fh)

    for card in cards:
        if card['id'] == id:
            cards.remove(card)
            break

    with open(cfg.CARDS_PATH, 'w', encoding='utf-8') as fh:
        json.dump(cards, fh, indent=4, ensure_ascii=False)
