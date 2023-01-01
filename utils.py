import json
from card import Card
from card_collection import CardCollection


def import_cards(path):
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
    file = open(destination_file_name, 'x')
    data = []
    for card in cards:
        card_data = {
            'id': card.id,
            'originLang': card.origin_lang_value,
            'learningLang': card.learning_lang_value,
            'category': card.category,
        }
        data.append(card_data)
    json.dump(data, file, indent=4, ensure_ascii=False)


def get_categorized_cards_collections(cards):
    categories_map = {'Wszystkie': CardCollection([], 'Wszystkie')}
    for card in cards:
        categories_map['Wszystkie'].add_cards([card])
        for category in card.categories:
            if category not in categories_map:
                categories_map[category] = CardCollection([card], category)
            else:
                categories_map[category].add_cards([card])
    return list(categories_map.values())
