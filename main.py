from card import Card
from card_collection import CardCollection
from app import App


def main():
    card1 = Card('autobus', 'bus')
    card2 = Card('kot', 'cat')
    card3 = Card('samochód', 'car')
    englishCards = CardCollection()
    englishCards.add_cards(cards=[card1, card2, card3])
    app = App()
    app.add_card_collections([englishCards])

    play = True
    while play:
        print()


if '__name__' == '__main__':
    main()
