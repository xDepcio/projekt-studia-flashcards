from exam import Exam
from utils import get_categorized_cards_collections, import_cards
from datetime import datetime
from time import time
from card import Card


def test_exam_end_with_empty_answers():
    cards = import_cards('tests/demo_cards.json')
    card_collections = get_categorized_cards_collections(cards)
    collection = ''
    for cc in card_collections:
        if cc.category == "Wszystkie":
            collection = cc

    exam = Exam(collection.draw_cards(5, False), 0)

    for card in exam.unanswered_cards:
        exam.answer_card(card, '')


def test_exam_generate_result():
    cards = import_cards('tests/demo_cards.json')
    card_collection = get_categorized_cards_collections(cards)[0]
    cards = card_collection.draw_cards(5, False)
    exam = Exam(cards, 2)
    unanswered = [*exam.unanswered_cards]
    for card in unanswered:
        exam.answer_card(card, '')
    result = exam.generate_result()

    assert len(result['answers']) == 5
    assert result['percentage'] == 0
    date_str = datetime.fromtimestamp(time()).strftime('%d-%m-%Y %H:%M')
    assert result['date'] == date_str


def test_exam_calculate_score():
    card1 = Card(1, 'a', '_a')
    card2 = Card(2, 'a', '_a')
    card3 = Card(3, 'a', '_a')
    card4 = Card(4, 'a', '_a')

    dummy_cards = [card1, card2, card3, card4]

    exam = Exam(dummy_cards, 2)
    exam.answer_card(card1, 'a')
    exam.answer_card(card2, '')
    exam.answer_card(card3, '')
    exam.answer_card(card4, '')

    correct, total, percentage = exam._calculate_score()
    assert correct == 1
    assert total == 4
    assert percentage == 25
