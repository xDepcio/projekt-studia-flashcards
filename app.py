class App:
    def __init__(self):
        self.correct_answers = 0
        self.wrong_answers = 0
        self.test = []
        self.card_collections = []

    def generate_learning_stats(self):
        # stuff about correct answers and wrong answers,
        # correct answers ratio, total guesses...
        pass

    def generate_app_stats():
        # info about total use time, average time each day...
        pass

    def add_test(self, cards_amount, time_limit, card_collection):
        pass

    def add_card_collections(self, card_collections):
        self.card_collections = [*self.card_collections, *card_collections]

    def random_draw_from_collection(self, card_collection):
        found_collection = self.card_collections[
            self.card_collections.index(card_collection)
        ]
        return found_collection.draw_cards(1)
