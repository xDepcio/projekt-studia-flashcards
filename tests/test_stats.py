from stats import Stats
from datetime import datetime
import time


def test_stats_init():
    stats = Stats('tests/demo_stats.json')
    assert len(stats.data['answers']['correct']) > 0
    assert len(stats.data['answers']['wrong']) > 0
    assert len(stats.data['exams']) > 0


def test_stats__answers_count():
    stats = Stats('tests/demo_stats.json')
    assert stats.answers_count() == 7


def test_stats_correct_answers_count():
    stats = Stats('tests/demo_stats.json')
    assert stats.correct_answers_count() == 4


def test_stats_wrong_answers_count():
    stats = Stats('tests/demo_stats.json')
    assert stats.wrong_answers_count() == 3


def test_stats_answers_accuracy():
    stats = Stats('tests/demo_stats.json')
    assert stats.answers_accuracy() == 57.14


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
