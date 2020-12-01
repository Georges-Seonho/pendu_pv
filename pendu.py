# -*-coding:utf-8 -*
import os 
from functions import *
os.chdir('../pendu_pv')

#variables declaration
guesses = 8
#player = input('Input your name here :')
player = 'plop' # while developing the game set the player name here
word = selectWordToGuess()
hiddenWord = createHiddenWord(word)
guessedLetter = []

getPlayerScore(player)

print(hiddenWord)

# while len(guessedLetter) <= 8:
#         if hiddenWord == word:
#             print('you won!!')
#             break

print('Guesses left: ' + str(guesses))