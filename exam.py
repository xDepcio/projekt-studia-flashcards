from random import choice
from datetime import datetime
from time import time
from typing import Tuple


class ExamNotCompleted(Exception):
    def __init__(self, title) -> None:
        super().__init__(title)


class Exam:
    def __init__(self, cards):
        self.unanswered_cards = cards
        self.answers = []
        self.is_completed = False
        date = datetime.fromtimestamp(time())
        date_str = date.strftime('%d-%m-%Y %H:%M')
        self.date = date_str

    def draw_card(self):
        """Return random Card() object from Exam().unanswered_cards array"""
        return choice(self.unanswered_cards)

    def answer_card(self, card, answer: str):
        """Removes answered Card() object from unanswered_cards
        and appends its answer to answers"""
        self.unanswered_cards.remove(card)
        answer_res = card.answer(answer)
        self.answers.append(answer_res)
        if len(self.unanswered_cards) <= 0:
            self.is_completed = True

    def generate_result(self) -> dict:
        """Generates dict containing exam results"""
        if not self.is_completed:
            raise ExamNotCompleted(
                'Cannot generate result of not finished exam'
            )

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

    def _calculate_score(self) -> Tuple[int, int, float]:
        """Returns tuple (
            exam_correct_answers_length,
            exam_answers_length,
            ratio
            ) where ration is exam_correct_answers_length/exam_answers_length
            rounded to two decimal points"""
        correct = [answer for answer in self.answers if answer.is_correct]
        percentage = round(len(correct)/len(self.answers)*100, 2)
        return len(correct), len(self.answers), percentage

    def __str__(self):
        return (
            f"unanswered: {self.unanswered_cards}\n"
            f"answers: {self.answers}\n"
            f"completed?: {self.is_completed}"
        )
