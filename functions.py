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
    
# def testLetter(letter):
    
# def testWord(word):

# def incrementPlayerScore(newScore): 

# def showBestScores(): 

