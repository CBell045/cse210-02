import random


class card:

    def __init__(self) -> None:
        pass
    
    def card_flip(self):
        self.value = random.randomint(1, 13)
        return self.value
