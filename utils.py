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
