from exam import Exam
from utils import get_categorized_cards_collections, import_cards


def test_exam_end_with_empty_answers():
    cards = import_cards('cards.json')
    card_collections = get_categorized_cards_collections(cards)
    collection = ''
    for cc in card_collections:
        if cc.category == "Wszystkie":
            collection = cc

    exam = Exam(collection.draw_cards(5, False), 0)

    for card in exam.unanswered_cards:
        exam.answer_card(card, '')
