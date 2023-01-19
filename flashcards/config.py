class Config:
    CARDS_PATH = 'flashcards/storage/cards.json'
    STATS_PATH = 'flashcards/storage/stats.json'
    POPUP_ANSWERS_COUNT = 5
    POPUP_MSG = (
        f'Od ostatniego testu minęło {POPUP_ANSWERS_COUNT} odpowiedzi. '
        'Może pora się sprawdzić?'
    )
    POPUP_TITLE = 'Przypomnienie'
    DEFAULT_DAYS_RANGE = 7
