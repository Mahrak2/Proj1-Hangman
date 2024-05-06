#!/usr/bin/env python3

class HMPlayer:
    """This is a generic player for the Hangman game."""
    def __init__(self, name: str) -> None:
        """Constructor, requires the player's name."""
        self.name = name
        self.lives = 5
        self.score = 0

    def propose_letter(self):
        """To be re-implemented in a derived class"""

    def __str__(self) -> str:
        """Returns a string representation of the player."""
        return "{} has {} points and {} lives left.".format(self.name, self.score, self.lives)

    def __lt__(self, other):
        """Comparison method to check if one player has fewer lives than another."""
        return self.lives < other.lives


