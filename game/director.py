from game.card import *

class director:

    def __init__(self) -> None:
        self.score = 300
        self.is_playing = True
        self.card = card.card_flip()
        pass

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_outputs()

    def get_inputs(self):
        print(f"The current card is {self.card}")
        new_card = card.card_flip()
        user_guess = input("Higher or lower? [h/l] ")
        while user_guess != 'h' or user_guess != 'l':
            user_guess = input("Invalid input. Please type h or l ")
        if user_guess == 'h':
            if self.card < new_card:
                self.score += 100
            else:
                self.score -= 75
        elif user_guess == 'l':
            if self.score > new_card:
                self.score -= 75
            else:
                self.score += 100
        self.card = new_card


    def do_outputs(self):
        print(f"Your score is {self.score}")
        self.is_playing = self.score > 0
        if self.is_playing == True:
            self.is_playing = input("Play again? [y/n]") == 'y'
    pass 