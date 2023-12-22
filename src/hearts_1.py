import random

SUITS = '♠', '♡', '♢', '♣'
RANKS = '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
DECK = list((s, r) for r in RANKS for s in SUITS)
PLAYERS = 'Player 1', 'Player 2', 'Player 3', 'Player 4'


def get_deck(shuffle=False):

    """
    Get a new deck of 52 cards.
    """

    new_deck = DECK.copy()
    if shuffle:
        random.shuffle(new_deck)

    return new_deck


def deal_hands(deck):

    """
    Deal the cards in the deck into four hands
    """

    return deck[0::4], deck[1::4], deck[2::4], deck[3::4]


def play():

    """
    Play a 4-player card game
    """

    deck = get_deck(shuffle=True)
    hands = {n: h for n, h in zip(PLAYERS, deal_hands(deck))}

    for name, cards in hands.items():
        card_str = ' '.join('{:3}'.format(s + r) for (s, r) in cards)
        print(f"{name}: {card_str}")


if __name__ == "__main__":
    play()

