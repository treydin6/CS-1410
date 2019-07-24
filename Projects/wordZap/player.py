from random import choice
from copy import copy

class Player:

    def __init__(self, name):
        self.mName = name
        self.mLetters = []
        for i in range(7):
            self.drawLetter()

    def getName(self):
        return self.mName

    def getLetters(self):
        return self.mLetters

    def drawLetter(self):
        letters = 'aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'
        letter = choice(letters)
        self.mLetters.append(letter)
        return letter

    def printLetters(self):
        new = ''
        for letter in self.mLetters:
            new += (letter + ' ')
        return new.strip()

    def checkWord(self, word):
        new_letters = copy(self.mLetters)           #make a copy of datamember letters
        for char in word:
            if not char in new_letters:
                return False
            
            for i in range(len(new_letters)):
                if new_letters[i] == char:
                    del new_letters[i]
                    break
        self.mLetters = new_letters
        return True



        
