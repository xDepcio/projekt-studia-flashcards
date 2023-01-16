from stats import Stats
from datetime import datetime
from card import Card
from exam import Exam
import json
from answer import Answer


def test_stats_init():
    stats = Stats('tests/dummy_data/demo_stats.json')
    assert len(stats.data['answers']['correct']) > 0
    assert len(stats.data['answers']['wrong']) > 0
    assert len(stats.data['exams']) > 0


def test_stats__answers_count():
    stats = Stats('tests/dummy_data/demo_stats.json')
    assert stats.answers_count() == 8


def test_stats_correct_answers_count():
    stats = Stats('tests/dummy_data/demo_stats.json')
    assert stats.correct_answers_count() == 5


def test_stats_wrong_answers_count():
    stats = Stats('tests/dummy_data/demo_stats.json')
    assert stats.wrong_answers_count() == 3


def test_stats_answers_accuracy():
    stats = Stats('tests/dummy_data/demo_stats.json')
    assert stats.answers_accuracy() == 62.5


def test_stats_exams_count():
    stats = Stats('tests/dummy_data/demo_stats.json')
    assert stats.exams_count() == 2


def test_stats_exams_avg_accuracy():
    stats = Stats('tests/dummy_data/demo_stats.json')
    assert stats.exams_avg_accuracy() == 40.00


def test_stats_app_use_time():
    stats = Stats('tests/dummy_data/demo_stats.json')
    use_time_stats = stats.app_use_time()
    assert use_time_stats == (5, 5, 0)


def test_stats_get_answers_date_range_count():
    stats = Stats('tests/dummy_data/demo_stats.json')
    correct, wrong, dates = stats.get_answers_date_range_count(
        4,
        datetime.strptime('22-12-2022 1:05', '%d-%m-%Y %H:%M')
    )
    assert len(dates) == 4
    assert len(correct) == 4
    assert len(wrong) == 4

    assert dates == [
        '19-12-2022',
        '20-12-2022',
        '21-12-2022',
        '22-12-2022'
        ]
    assert correct == [2, 1, 1, 0]
    assert wrong == [3, 0, 0, 0]


def test_stats_get_days_list():
    stats = Stats('tests/dummy_data/demo_stats.json')
    days = stats._get_days_list(1234567, 3, '%d-%m-%Y %H:%M')
    assert days == ['13-01-1970 07:56', '14-01-1970 07:56', '15-01-1970 07:56']


def test_stats_save_exam():
    start_data = {
        "answers": {
            "correct": [
                {
                    "originLang": "Samochód",
                    "learningLang": "Car",
                    "date": "19-12-2022 01:15"
                }
            ],
            "wrong": [
                {
                    "originLang": "Samolot",
                    "learningLang": "Airplane",
                    "date": "19-12-2022 01:57"
                }
            ]
        },
        "exams": [
            {
                "correct": 0,
                "total": 1,
                "percentage": 0.0,
                "answers": [
                    {
                        "expected": "Samolot",
                        "given": "sdasa",
                        "toBeGuessed": "Airplane",
                        "isCorrect": False
                    }
                ],
                "date": "22-12-2022 19:29"
            }
        ],
        "answersToLastExam": 2
    }


    path = 'tests/dummy_data/test_stats_save_exam.json'
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(start_data, fh, ensure_ascii=False, indent=4)
    stats = Stats(path)
    card1 = Card(1, 'a', '_a')
    card2 = Card(2, 'a', '_a')
    dummy_cards = [card1, card2]
    exam = Exam(dummy_cards)
    exam.answer_card(card1, '')
    exam.answer_card(card2, 'a')
    ex_result = exam.generate_result()
    stats.save_exam(exam)

    with open(path, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
        assert len(data['exams']) == 2
        assert data['exams'][1] == ex_result


def test_stats_save_answer():
    start_data = {
        "answers": {
            "correct": [
                {
                    "originLang": "Samochód",
                    "learningLang": "Car",
                    "date": "19-12-2022 01:15"
                }
            ],
            "wrong": [
                {
                    "originLang": "Samolot",
                    "learningLang": "Airplane",
                    "date": "19-12-2022 01:57"
                }
            ]
        }
    }
    path = 'tests/dummy_data/test_stats_save_answer.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(start_data, f, ensure_ascii=False, indent=4)

    stats = Stats(path)
    card1 = Card(1, 'a', '_a')
    ans = Answer(card1, 'a')
    stats.save_answer(ans)

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        assert data['answers']['wrong'] == [
            {
                "originLang": "Samolot",
                "learningLang": "Airplane",
                "date": "19-12-2022 01:57"
            }
        ]
        assert data['answers']['correct'][1] == {
                "originLang": "a",
                "learningLang": "_a",
                "date": ans.date_str()
            }
