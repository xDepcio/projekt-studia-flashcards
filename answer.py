from datetime import datetime
from time import time


class Answer:
    def __init__(self, card, answer):
        self.expected = card.origin_lang_value
        self.given = answer
        self.to_be_guessed = card.learning_lang_value
        self.is_correct = card.evaluate_answer(answer)
        date = datetime.fromtimestamp(time())
        date = f'{date.year}-{date.month}-{date.day} {date.hour}:{date.minute}'
        self.date = date
