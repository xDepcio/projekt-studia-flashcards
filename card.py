class Card:
    def __init__(
        self,
        id,
        origin_lang_value,
        learning_lang_value,
        categories=None,
        popularity=None
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

    def evaluate_answer(self, answer):
        answer_bool = answer.lower() == self.origin_lang_value.lower()
        self._handle_answer(answer_bool)
        self._save()
        return answer_bool

    def _handle_answer(self, is_correct):
        if is_correct:
            self.popularity = self.popularity * 0.75
        else:
            self.popularity = self.popularity * 1.5

    def _save(self):
        pass

    def __repr__(self):
        return str({
            'id': self.id,
            'origin_lang_value': self.origin_lang_value,
            'learning_lang_value': self.learning_lang_value,
            'categories': self.categories,
            'popularity': self.popularity,
        })
