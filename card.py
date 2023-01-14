from answer import Answer
from config import Config
import json


class Card:
    def __init__(
        self,
        id: int,
        origin_lang_value: str,
        learning_lang_value: str,
        categories=None,
        popularity: float = None
    ):
        self.id = id
        self.origin_lang_value = origin_lang_value
        self.learning_lang_value = learning_lang_value
        if categories is None:
            self.categories = []
        else:
            self.categories = categories
        if popularity is None:
            self.popularity = 0.1
        else:
            self.popularity = popularity
            if type(self.popularity) is not float:
                raise ValueError('popularity is be float in range 0.01 - 0.99')
            if (popularity < 0.01 or popularity > 0.99):
                raise ValueError('popularity is be float in range 0.01 - 0.99')

    def answer(self, answer: str):
        """Compares normalized answer to correct value, changes popularity
        based on answer and returns new Answer() object"""
        answer_bool = self.evaluate_answer(answer)
        self._handle_answer(answer_bool)
        self._save(Config.CARDS_PATH)
        return Answer(self, answer)

    def evaluate_answer(self, answer: str):
        """Return True if normalized answer matches normalized origin,
        False otherwise"""
        return answer.lower() == self.origin_lang_value.lower()

    def _handle_answer(self, is_correct: bool):
        """Change popularity based on is_correct bool value"""
        if is_correct:
            self.popularity = max(self.popularity * 0.75, 0.01)
        else:
            self.popularity = min(self.popularity * 1.8, 0.99)

    def _save(self, path):
        """Save card data to file"""
        cards = []
        with open(path, 'r', encoding='utf-8') as fh:
            cards = json.load(fh)
            cards[
                self.__keyed_index(cards, lambda ele: ele['id'] == self.id)
            ]['popularity'] = self.popularity

        with open(path, 'w', encoding='utf-8') as fh:
            json.dump(cards, fh, indent=4, ensure_ascii=False)

    def __keyed_index(self, array, callback):
        for i, ele in enumerate(array):
            if callback(ele):
                return i
