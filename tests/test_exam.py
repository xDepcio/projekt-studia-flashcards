from exam import Exam, ExamNotCompleted
from utils import get_categorized_cards_collections, import_cards
from datetime import datetime
from time import time
from card import Card
import pytest


def test_exam_init():
    card1 = Card(1, 'a', '_a')
    card2 = Card(2, 'a', '_a')
    card3 = Card(3, 'a', '_a')
    card4 = Card(4, 'a', '_a')
    dummy_cards = [card1, card2, card3, card4]
    exam = Exam(dummy_cards)

    assert exam.answers == []
    assert exam.date == datetime.strftime(
        datetime.fromtimestamp(time()), '%d-%m-%Y %H:%M')
    assert exam.is_completed is False
    assert exam.unanswered_cards == dummy_cards


def test_exam_end_with_empty_answers():
    cards = import_cards('tests/dummy_data/demo_cards.json')
    card_collections = get_categorized_cards_collections(cards)
    collection = ''
    for cc in card_collections:
        if cc.category == "Wszystkie":
            collection = cc

    exam = Exam(collection.draw_cards(5, False))

    for card in exam.unanswered_cards:
        exam.answer_card(card, '')


def test_exam_generate_result():
    cards = import_cards('tests/dummy_data/demo_cards.json')
    card_collection = get_categorized_cards_collections(cards)[0]
    cards = card_collection.draw_cards(5, False)
    exam = Exam(cards)
    unanswered = [*exam.unanswered_cards]
    for card in unanswered:
        exam.answer_card(card, '')
    exam.is_completed = True
    result = exam.generate_result()

    assert len(result['answers']) == 5
    assert result['percentage'] == 0
    date_str = datetime.fromtimestamp(time()).strftime('%d-%m-%Y %H:%M')
    assert result['date'] == date_str


def test_exam_generate_result_not_completed():
    card1 = Card(1, 'a', '_a')
    card2 = Card(2, 'a', '_a')
    card3 = Card(3, 'a', '_a')
    card4 = Card(4, 'a', '_a')
    dummy_cards = [card1, card2, card3, card4]
    exam = Exam(dummy_cards)

    with pytest.raises(ExamNotCompleted):
        exam.generate_result()


def test_exam_answer_card():
    card1 = Card(1, 'a', '_a')
    card2 = Card(2, 'a', '_a')
    card3 = Card(3, 'a', '_a')
    card4 = Card(4, 'a', '_a')
    dummy_cards = [card1, card2, card3, card4]
    exam = Exam(dummy_cards)

    exam.answer_card(card1, 'a')
    assert card1 not in exam.unanswered_cards
    exam.answer_card(card2, 'a')
    exam.answer_card(card3, 'a')
    exam.answer_card(card4, 'a')
    assert exam.unanswered_cards == []
    assert len(exam.answers) == 4


def test_exam_calculate_score():
    card1 = Card(1, 'a', '_a')
    card2 = Card(2, 'a', '_a')
    card3 = Card(3, 'a', '_a')
    card4 = Card(4, 'a', '_a')
    dummy_cards = [card1, card2, card3, card4]
    exam = Exam(dummy_cards)

    exam.answer_card(card1, 'a')
    exam.answer_card(card2, '')
    exam.answer_card(card3, '')
    exam.answer_card(card4, '')

    correct, total, percentage = exam._calculate_score()
    assert correct == 1
    assert total == 4
    assert percentage == 25


def test_exam_draw_card():
    card1 = Card(1, 'a', '_a')
    card2 = Card(2, 'a', '_a')
    card3 = Card(3, 'a', '_a')
    card4 = Card(4, 'a', '_a')
    dummy_cards = [card1, card2, card3, card4]
    exam = Exam(dummy_cards)

    card = exam.draw_card()
    assert card in dummy_cards
    exam.answer_card(card1, 'a')
    exam.answer_card(card2, 'a')
    exam.answer_card(card3, 'a')
    exam.answer_card(card4, 'a')
    assert exam.is_completed is True
