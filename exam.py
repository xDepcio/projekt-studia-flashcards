from random import choice


class Exam:
    def __init__(self, cards, time_limit):
        self.unanswered_cards = cards
        self.answers = []
        self.is_completed = False

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
            ]
        }

    def _calculate_score(self):
        correct = [answer for answer in self.answers if answer.is_correct]
        percentage = len(correct)/len(self.answers)*100
        return len(correct), len(self.answers), percentage
