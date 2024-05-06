
#!/usr/bin/env python3
import sys
import os

# Get the absolute path to the Hangman directory
hangman_dir = "/home/malhosani/Desktop/Proj1-Hangman/Hangman"

# Add the 'Hangman' directory to the Python path
sys.path.append(hangman_dir)

# Import Hangman modules after adding the path
from HMPlayer import HMPlayer
from HMHumanPlayer import HMHumanPlayer 
from HMGame import HMGame

# Your test functions and code here

def test1():
    p1 = HMHumanPlayer("Alice")
    p2 = HMHumanPlayer("Bob")
    players = [p1, p2]
    game = HMGame(players)
    game.play()

if __name__ == "__main__":
    test1()
