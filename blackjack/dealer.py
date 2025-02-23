import random
from turtle import Screen
from card import Card
from settings import DEALER_POSITION


class Dealer:
    def __init__(self, deck):
        self.deck = deck
        self.cards = []
        self.pos = DEALER_POSITION
        self.screen = Screen()

    def deal_card(self, player):
        # pick a random card
        random_suit = random.choice(self.deck)
        suit = list(random_suit)[0]
        random_card = random.choice(random_suit[suit])
        card = list(random_card)[0]
        point = random_card[card]


        new_card = Card(card, point)

        # deal animation
        if len(player.cards) == 0:
            new_card.goto(0, player.pos)
            player.cards.append(new_card)
        else:
            # hide the second card
            if len(player.cards) == 1 and player.pos == DEALER_POSITION:
                new_card.hideturtle()
                new_card.speed(9)
                new_card.goto(player.cards[-1].xcor() + 24, player.pos)

                back_card = Card("back-card.gif", 0)
                back_card.goto(player.cards[-1].xcor() + 24, player.pos)
            else:
                new_card.goto(player.cards[-1].xcor() + 24, player.pos)

            # move the cards to the left
            for p_card in player.cards:
                p_card.goto(p_card.xcor() - 24, player.pos)
            player.cards.append(new_card)






