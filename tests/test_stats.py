from stats import Stats


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
