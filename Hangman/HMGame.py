#!/usr/bin/env python3 

import random
from HMPlayer import HMPlayer

class HMGame:
    """A class to represent a game of Hangman."""
    def __init__(self, players: list) -> None:
        self.word = None
        self.players = players
        self.guessed_letters = []

    def display_word(self):
        """Displays the word with guessed letters."""
        display = ""
        for c in self.word:
            if c in self.guessed_letters:
                display += c
            else:
                display += '_'
        return display

    def play(self):
        """Starts the Hangman game."""
        for p in self.players:
            self.word = random.choice(["dog", "cat", "house", "pencil", "music", "banana", "hospital"])
            self.guessed_letters = []
            while p.lives > 0 and self.word != self.display_word():
                print("----------------------------")
                self.turn(p)
            if self.word == self.display_word():
                print("Congrats {}, you won!".format(p.name))
            else:
                print("Player {} lost the game".format(p.name))

        winner = max(self.players)
        print("The player that has won the game is {}".format(winner.name))

    def turn(self, p: HMPlayer) -> None:
        """Performs a turn in the Hangman game."""
        print("Player {}. Word: {}".format(p.name, self.display_word()))
        l = p.propose_letter()
        print("Player {} proposes letter: {}".format(p.name, l))
        if l in self.word and l not in self.guessed_letters:
            print("Good guess!\n")
            self.guessed_letters.append(l)
        else:
            print("Wrong guess!\n")
            p.lives -= 1
