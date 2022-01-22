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
        print("Your starting score is 300")
        while self.is_playing:
            self.get_inputs()
            self.do_outputs()
        print(f"Your final score was {self.score}")

        
    def get_inputs(self):
        print(f"\nThe current card is {self.card}")
        new_card = card.card_flip()
        user_guess = input("Higher or lower? [h/l] ")
        while user_guess != 'h' and user_guess != 'l':
            user_guess = input("Invalid input. Please type h or l ")
        if user_guess == 'h':
            if self.card < new_card:
                self.score += 100
            else:
                self.score -= 75
        elif user_guess == 'l':
            if self.card < new_card:
                self.score -= 75
            else:
                self.score += 100

        print(f"Next card was {new_card}")
        self.card = new_card



    def do_outputs(self):
        print(f"Your score is {self.score}")
        self.is_playing = self.score > 0
        if self.is_playing == True:
            play_again = input("Play again? [y/n] ")
            while play_again != 'y' and play_again != 'n':
                play_again = input("Invalid input... [y/n] ")
            self.is_playing = play_again == 'y'