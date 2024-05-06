#!/usr/bin/env python3 

from HMPlayer import HMPlayer
import random

class HMAIPlayer(HMPlayer):
    """A class to represent an AI player for the hangman game."""
    def __init__(self, name: str) -> None:
        super().__init__(name + "_bot")
        self.proposed_letters = []

    def propose_letter(self) -> str:
        """Proposes a letter randomly."""
        letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        while letter in self.proposed_letters:
            letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        self.proposed_letters.append(letter)
        return letter
