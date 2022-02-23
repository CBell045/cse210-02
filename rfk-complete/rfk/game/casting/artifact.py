import random
from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._message = ""

        text = random.choice(['*' , '[]'])
        self.set_text(text)
        CELL_SIZE = 15
        FONT_SIZE = 15
        COLS = 60
        ROWS = 40
        x = random.randint(1, COLS - 1)
        y = 1 #random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        self.set_color(color)
        self.set_position(position)
        self.set_velocity(Point(0, 1))
        



        
    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message