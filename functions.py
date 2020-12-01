# -*-coding:utf-8 -*
from data import words, bestScores
from random import randint

def getPlayerScore(player): 
    if player in bestScores:
        print('Your best score yet: ' + str(bestScores[player]))
    else:
        bestScores[player] = 0 
        print(bestScores)

def selectWordToGuess():
    i = randint(0, len(words)-1)
    return words[i]

def createHiddenWord(word):
    result = ''
    for letter in word: 
        result += '*'
    return result
    
def getLetter(word, hiddenWord):
    letter = input('Enter a letter:')
    secret = ''
    i = -1
    if letter in word and len(letter) == 1 and letter.isalpha(): 
        for char in word:
            i += 1
            if char == letter:
                secret += letter
            elif hiddenWord[i] != '*':
                secret += hiddenWord[i]
            else:
                secret += '*'
        return 'True', letter, secret
    return 'False', letter, hiddenWord
    
# def testWord(word):

# def incrementPlayerScore(newScore): 

# def showBestScores(): 

