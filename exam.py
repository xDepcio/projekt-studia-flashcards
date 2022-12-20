class Exam:
    def __init__(self, cards_amount, time_limit, card_collection, difficulty):
        self.cards_amount = cards_amount
        self.time_limit = time_limit
        self.cards = card_collection.draw_cards(cards_amount)
        self.is_finished = False
        self.complete_time = None
        self.difficulty = difficulty

    def generate_test_result(self):
        pass
