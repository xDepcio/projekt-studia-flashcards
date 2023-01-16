from answer import Answer
from card import Card
from datetime import datetime
from time import time


def test_answer_init_good_answ():
    card = Card(1, 'a', 'b')
    ans = Answer(card, 'a')
    date = datetime.fromtimestamp(time())
    assert ans.date == date
    assert ans.expected == 'a'
    assert ans.given == 'a'
    assert ans.to_be_guessed == 'b'
    assert ans.is_correct is True


def test_answer_init_bad_answ():
    card = Card(1, 'a', 'b')
    ans = Answer(card, 'c')
    date = datetime.fromtimestamp(time())
    assert ans.date == date
    assert ans.expected == 'a'
    assert ans.given == 'c'
    assert ans.to_be_guessed == 'b'
    assert ans.is_correct is False


def test_answer_date_str():
    card = Card(1, 'a', 'b')
    ans = Answer(card, 'c')
    date = datetime.fromtimestamp(time())
    assert ans.date_str() == date.strftime('%d-%m-%Y %H:%M')
    assert ans.date_str('%d-%m-%Y') == date.strftime('%d-%m-%Y')
