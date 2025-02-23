import time
from turtle import Screen
from button import Button
from card import Card
from dealer import Dealer, DEALER_POSITION
from player import Player
from scoreboard import Scoreboard
from settings import SCREEN_WIDTH, TITLE, TABLE_BG, HIT_BUTTON_POS_X, STAND_BUTTON_POS_X, HIT_BUTTON_POS_Y, \
    STAND_BUTTON_POS_Y, HIT_TEXT, STAND_TEXT, HIT_COLOR, STAND_COLOR, SCREEN_HEIGHT, PLAYER_WIN_COLOR, \
    PLAYER_LOSE_COLOR, BLACKJACK_COLOR



class Blackjack:
    def __init__(self):

        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgpic(TABLE_BG)
        self.screen.title(TITLE)

        self.deck_of_cards = [
            {"clubs": [
                {"ace-of-clubs.gif": 11},
                {"king-of-clubs.gif": 10},
                {"queen-of-clubs.gif": 10},
                {"jack-of-clubs.gif": 10},
                {"ten-of-clubs.gif": 10},
                {"nine-of-clubs.gif": 9},
                {"eight-of-clubs.gif": 8},
                {"seven-of-clubs.gif": 7},
                {"six-of-clubs.gif": 6},
                {"five-of-clubs.gif": 5},
                {"four-of-clubs.gif": 4},
                {"three-of-clubs.gif": 3},
                {"two-of-clubs.gif": 2}
            ]},
            {"diamonds": [
                {"ace-of-diamonds.gif": 11},
                {"king-of-diamonds.gif": 10},
                {"queen-of-diamonds.gif": 10},
                {"jack-of-diamonds.gif": 10},
                {"ten-of-diamonds.gif": 10},
                {"nine-of-diamonds.gif": 9},
                {"eight-of-diamonds.gif": 8},
                {"seven-of-diamonds.gif": 7},
                {"six-of-diamonds.gif": 6},
                {"five-of-diamonds.gif": 5},
                {"four-of-diamonds.gif": 4},
                {"three-of-diamonds.gif": 3},
                {"two-of-diamonds.gif": 2}
            ]},
            {"spades": [
                {"ace-of-spades.gif": 11},
                {"king-of-spades.gif": 10},
                {"queen-of-spades.gif": 10},
                {"jack-of-spades.gif": 10},
                {"ten-of-spades.gif": 10},
                {"nine-of-spades.gif": 9},
                {"eight-of-spades.gif": 8},
                {"seven-of-spades.gif": 7},
                {"six-of-spades.gif": 6},
                {"five-of-spades.gif": 5},
                {"four-of-spades.gif": 4},
                {"three-of-spades.gif": 3},
                {"two-of-spades.gif": 2}
            ]},
            {"hearts": [
                {"ace-of-hearts.gif": 11},
                {"king-of-hearts.gif": 10},
                {"queen-of-hearts.gif": 10},
                {"jack-of-hearts.gif": 10},
                {"ten-of-hearts.gif": 10},
                {"nine-of-hearts.gif": 9},
                {"eight-of-hearts.gif": 8},
                {"seven-of-hearts.gif": 7},
                {"six-of-hearts.gif": 6},
                {"five-of-hearts.gif": 5},
                {"four-of-hearts.gif": 4},
                {"three-of-hearts.gif": 3},
                {"two-of-hearts.gif": 2}
            ]}
        ]
        self.add_shapes()

        self.dealer = Dealer(self.deck_of_cards)
        self.player = Player()
        self.scoreboard = Scoreboard()

        self.hit_button = Button(HIT_BUTTON_POS_X, HIT_BUTTON_POS_Y, HIT_TEXT, HIT_COLOR)
        self.stand_button = Button(STAND_BUTTON_POS_X, STAND_BUTTON_POS_Y, STAND_TEXT, STAND_COLOR)

        Card("stacked-cards.gif", 0)
        self.screen.onclick(fun=self.button_click)


    def start_game(self):
        # deal two cards to each player and update the score
        for num in range(2):
            self.dealer.deal_card(self.dealer)
            if num == 0:
                self.scoreboard.update_dealer(self.dealer.cards[0].point)
            self.dealer.deal_card(self.player)
            self.scoreboard.update_player(self.player.cards[-1].point)


        if "ace" in self.dealer.cards[0].shape() and "ace" in self.dealer.cards[1].shape():
            self.scoreboard.dealer_score = 0
            self.dealer.cards[-1].point = 1
            self.scoreboard.update_dealer(11+1)

        if "ace" in self.player.cards[0].shape() and "ace" in self.player.cards[1].shape():
            self.scoreboard.player_score = 0
            self.player.cards[-1].point = 1
            self.scoreboard.update_player(11+1)

        # check for blackjack
        if self.scoreboard.player_score == 21 or (self.dealer.cards[-1].point + self.scoreboard.dealer_score) == 21:
            time.sleep(0.5)
            self.reveal_card()
            if self.scoreboard.player_score == 21:
                self.scoreboard.game_over(["BLACK JACK!", "player"], BLACKJACK_COLOR)
            else:
                self.scoreboard.game_over(["BLACK JACK!", "dealer"], BLACKJACK_COLOR)
            self.restart_game()

        self.screen.mainloop()


    def button_click(self, x, y):

        if STAND_BUTTON_POS_X < x < STAND_BUTTON_POS_X + 100 and STAND_BUTTON_POS_Y < y < STAND_BUTTON_POS_Y + 40:
            self.stand()

        if HIT_BUTTON_POS_X < x < HIT_BUTTON_POS_X + 100 and HIT_BUTTON_POS_Y < y < HIT_BUTTON_POS_Y + 40:
            self.hit()

    def reveal_card(self):
        # reveal the hidden card
        for card in self.screen.turtles():
            if "back-card" in card.shape():
                card.goto(card.xcor(), 400)
                self.dealer.cards[1].goto(card.xcor(), 400)
                self.dealer.cards[1].showturtle()
                self.dealer.cards[1].goto(card.xcor(), DEALER_POSITION)
                self.scoreboard.update_dealer(self.dealer.cards[1].point)

    def compare(self):
        if self.scoreboard.dealer_score > 21:
            self.scoreboard.game_over(["You win!", "Bust"], PLAYER_WIN_COLOR)
        elif self.scoreboard.dealer_score > self.scoreboard.player_score:
            self.scoreboard.game_over(["You lose!", "Dealer wins!"], PLAYER_LOSE_COLOR)
        elif self.scoreboard.dealer_score == self.scoreboard.player_score:
            self.scoreboard.game_over(["Push"], PLAYER_LOSE_COLOR)
        else:
            self.scoreboard.game_over(["You win!", "Dealer loses!"], PLAYER_WIN_COLOR)

    def stand(self):
        self.reveal_card()
        time.sleep(0.5)

        # deal cards until the score reaches above 17
        while self.scoreboard.dealer_score < 17:
            self.dealer.deal_card(self.dealer)
            if "ace" in self.dealer.cards[-1].shape():
                if (self.scoreboard.dealer_score + 11) > 21:
                    self.dealer.cards[-1].point = 1
                    self.scoreboard.update_dealer(self.dealer.cards[-1].point)
                else:
                    self.scoreboard.update_dealer(self.dealer.cards[-1].point)
            else:
                self.scoreboard.update_dealer(self.dealer.cards[-1].point)


        self.compare()

        self.restart_game()

    def hit(self):
        self.dealer.deal_card(self.player)

        if "ace" in self.player.cards[-1].shape():
            if (self.scoreboard.player_score + 11) > 21:
                self.player.cards[-1].point = 1
                self.scoreboard.update_player(self.player.cards[-1].point)
            else:
                self.scoreboard.update_player(self.player.cards[-1].point)
        else:
            self.scoreboard.update_player(self.player.cards[-1].point)

        if self.scoreboard.player_score > 21:
            self.reveal_card()
            self.scoreboard.game_over(["Bust", "Dealer wins!"], PLAYER_LOSE_COLOR)
            self.restart_game()

    def restart_game(self):
        # restart the game

        time.sleep(5)
        # reset score
        self.scoreboard.reset_score()

        # remove the cards
        self.screen.tracer(0)
        for _ in range(100):
            for card in self.dealer.cards:
                card.setheading(90)
                card.forward(2)
            self.screen.update()

        for _ in range(300):
            for card in self.player.cards:
                card.setheading(90)
                card.forward(2)
            self.screen.update()
        self.screen.tracer(1)

        self.dealer.cards.clear()
        self.player.cards.clear()
        self.screen.turtles().clear()

        # start game
        time.sleep(1)
        self.start_game()

    def add_shapes(self):
        for suit in self.deck_of_cards:
            suit_key = list(suit.keys())[0]
            cards = suit[suit_key]
            for card in cards:
                card_gif = list(card.keys())[0]
                self.screen.addshape(f"./assets/cards/{card_gif}")

        self.screen.addshape(f"./assets/cards/stacked-cards.gif")
        self.screen.addshape(f"./assets/cards/back-card.gif")
