from random import choice
from datetime import datetime
from time import time


class Exam:
    def __init__(self, cards, time_limit):
        self.unanswered_cards = cards
        self.answers = []
        self.is_completed = False
        date = datetime.fromtimestamp(time())
        date = f'{date.year}-{date.month}-{date.day} {date.hour}:{date.minute}'
        self.date = date

    def draw_card(self):
        if len(self.unanswered_cards) <= 0:
            self.is_completed = True
            return
        return choice(self.unanswered_cards)

    def answer_card(self, card, answer):
        self.unanswered_cards.remove(card)
        answer_res = card.answer(answer)
        self.answers.append(answer_res)

    def generate_result(self):
        correct, total, percentage = self._calculate_score()
        return {
            "correct": correct,
            "total": total,
            "percentage": percentage,
            "answers": [
                {
                    "expected": answer.expected,
                    "given": answer.given,
                    "toBeGuessed": answer.to_be_guessed,
                    "isCorrect": answer.is_correct
                }
                for answer in self.answers
            ],
            "date": self.date
        }

    def _calculate_score(self):
        correct = [answer for answer in self.answers if answer.is_correct]
        percentage = round(len(correct)/len(self.answers)*100, 2)
        return len(correct), len(self.answers), percentage

    def __str__(self):
        return (
            f"unanswered: {self.unanswered_cards}\n"
            f"answers: {self.answers}\n"
            f"completed?: {self.is_completed}"
        )