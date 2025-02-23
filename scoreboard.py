import time
from turtle import Turtle

from settings import TEXT_FONT, SCORE_COLOR, DEALER_SCORE_POS, PLAYER_SCORE_POS, GAMER_OVER_FONT, \
    BLACKJACK_FONT, PLAYER_LOSE_COLOR, PLAYER_WIN_COLOR


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.dealer_score = 0
        self.speed(9)
        self.hideturtle()
        self.penup()
        self.show_score()

    def update_dealer(self, score):
        self.dealer_score += score
        self.show_score()
    def update_player(self, score):
        self.player_score += score
        self.show_score()
    def show_score(self):
        self.screen.tracer(0)
        self.clear()
        self.color(SCORE_COLOR)
        self.goto(DEALER_SCORE_POS)
        self.write(self.dealer_score, align="center", font=TEXT_FONT)
        self.goto(PLAYER_SCORE_POS)
        self.write(self.player_score, align="center", font=TEXT_FONT)
        self.screen.tracer(1)


    def game_over(self, msg, text_color):
        self.color(text_color)

        if msg[0] != "Push" and msg[0] != "BLACK JACK!":
            msg_player = msg[0]
            msg_dealer = msg[1]

            self.goto(0, -110)
            self.write(msg_player, align="center", font=GAMER_OVER_FONT)
            self.goto(0, 80)
            self.write(msg_dealer, align="center", font=GAMER_OVER_FONT)
        else:
            msg_text = msg[0]
            if msg_text == "Push":
                self.goto(0, 0)
                self.write(msg_text, align="center", font=GAMER_OVER_FONT)

            elif msg_text == "BLACK JACK!":
                self.goto(0, 0)
                self.write(msg_text, align="center", font=BLACKJACK_FONT)
                time.sleep(3)
                self.clear()
                if msg[1] == "player":
                    self.color(PLAYER_WIN_COLOR)
                    self.write("You win!", align="center", font=GAMER_OVER_FONT)
                else:
                    self.color(PLAYER_LOSE_COLOR)
                    self.write("You lose!", align="center", font=GAMER_OVER_FONT)



    def reset_score(self):
        self.player_score = 0
        self.dealer_score = 0
        self.show_score()



