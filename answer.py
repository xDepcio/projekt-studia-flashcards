from datetime import datetime
from time import time


class Answer:
    def __init__(self, card, answer):
        self.expected = card.origin_lang_value
        self.given = answer
        self.to_be_guessed = card.learning_lang_value
        self.is_correct = card.evaluate_answer(answer)
        dt = datetime.fromtimestamp(time())
        date_str = dt.strftime('%d-%m-%Y %H:%M')
        self.date = date_str
