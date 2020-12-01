# -*-coding:utf-8 -*
from random import randint
import pickle



words = ['hello']
bestScores = {}

with open('data.py', 'rb') as datas:
     monDepickler = pickle.Unpickler(datas)
     bestScores = monDepickler.load()

#, 'bonjour', 'hallo', 'gutentag', 'hi', 'bonsoir'

def getPlayerScore(player): 
    if player in bestScores:
        print('Your best score yet: ' + str(bestScores[player]))
    else:
        bestScores[player] = 0 
        print('Happy first game!!')

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

def playAgain():
    motiv = input('Type 0 to play again :')
    if motiv == 'O' or motiv == 'o' or motiv == '0':
        return True 
    

def savePlayerScore(newScore, currentPlayer): 
    if newScore > bestScores[currentPlayer]: 
        bestScores[currentPlayer] = newScore
        with open('data.py', 'wb') as datas:
            mon_pickler = pickle.Pickler(datas)
            mon_pickler.dump(bestScores)

