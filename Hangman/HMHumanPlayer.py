#!/usr/bin/env python3 


from HMPlayer import HMPlayer
from time import sleep

class HMHumanPlayer(HMPlayer):
    """A class to represent a Hangman human player."""
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def propose_letter(self) -> str:
        """Proposes a letter for the Hangman game."""
        sleep(1)
        letter = ""
        while len(letter) != 1:
            letter = input("Propose a letter:").lower()
        return letter
