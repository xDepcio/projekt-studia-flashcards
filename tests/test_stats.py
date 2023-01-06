from stats import Stats
from datetime import datetime


def test_stats_init():
    stats = Stats('tests/demo_stats.json')
    assert len(stats.data['answers']['correct']) > 0
    assert len(stats.data['answers']['wrong']) > 0
    assert len(stats.data['exams']) > 0


def test_stats__answers_count():
    stats = Stats('tests/demo_stats.json')
    assert stats.answers_count() == 8


def test_stats_correct_answers_count():
    stats = Stats('tests/demo_stats.json')
    assert stats.correct_answers_count() == 5


def test_stats_wrong_answers_count():
    stats = Stats('tests/demo_stats.json')
    assert stats.wrong_answers_count() == 3


def test_stats_answers_accuracy():
    stats = Stats('tests/demo_stats.json')
    assert stats.answers_accuracy() == 62.5


def test_stats_exams_count():
    stats = Stats('tests/demo_stats.json')
    assert stats.exams_count() == 2


def test_stats_exams_avg_accuracy():
    stats = Stats('tests/demo_stats.json')
    assert stats.exams_avg_accuracy() == 40.00


def test_stats_app_use_time():
    stats = Stats('tests/demo_stats.json')
    use_time_stats = stats.app_use_time()
    assert use_time_stats == (5, 5, 0)


def test_stats_get_answers_date_range_count():
    stats = Stats('tests/demo_stats.json')
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
