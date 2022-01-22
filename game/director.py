class director:

    def __init__(self) -> None:
        self.score = 300
        self.is_playing = True

        pass

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs():
        pass
    def do_updates():
        pass
    def do_outputs():
        pass
    pass 