# -*-coding:utf-8 -*
import os 
from functions import *
os.chdir('../pendu_pv')

#variables declaration
continuPlaying = True
currentScore = 0
guesses = 8
player = input('Input your name here :')
#player = 'plop' # while developing the game set the player name here
word = selectWordToGuess()
hiddenWord = createHiddenWord(word)
guessedLetter = []

# game starts here
getPlayerScore(player)
print('Secret word: ' + hiddenWord)

while guesses > 0 and continuPlaying == True:
        currentResult, currentLetter, updatedHiddenWord = getLetter(word, hiddenWord)
        try:
            if currentResult == 'False': 
                guesses -= 1
                if currentLetter not in guessedLetter and currentLetter.isalpha(): 
                    guessedLetter.append(currentLetter)
                print('Nop, you loose one chance.')

            else:
                guesses -= 1
                guessedLetter.append(currentLetter)
                hiddenWord = updatedHiddenWord

            if hiddenWord == word:
                print('you won!!')
                currentScore += guesses
                continuPlaying = playAgain()
                if continuPlaying == True:
                    guesses = 8
                    word = selectWordToGuess()
                    hiddenWord = createHiddenWord(word)
                    guessedLetter = []
                else:
                    break
                
        finally:
            print('Secret word: ' + hiddenWord)
            print( 'You tried the letters : ' + ', '.join(guessedLetter))

print('thank you for playing')
savePlayerScore(currentScore, player)
             


