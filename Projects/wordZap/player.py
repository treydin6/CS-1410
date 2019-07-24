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
        letters = copy(self.mLetters)
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        self.letters = letters
        return True



        # string = ''
		# list1 = self.getLetters()
		# leng = len(list1)
		# if len(word) > len(list1):
		# 	return False
		# for i in range(len(word)):
		# 	for j in range(leng):
		# 		if word[i] == list1[j]:
		# 			string += word[i]
		# 			list1.pop(j)
		# 			leng -= 1
		# 			break
		# if string == word:
		# 	self.mLetters = list1
		# 	return True
		# else:
		# 	return False



        # letters = copy(self.mLetters)
        # for letter in word:
        #     if letter in letters:
        #         letters.remove(letter)
        #     else:
        #         return False
        # self.letters = letters
        # return True
        
        





# def checkWord(word):
#     1) copy the letters
#     2) check if any of the letter work or dont work
#         - remove letter as you go
#     3)make a deep copy
#         a = [1,3,5,3]
#         b = a[:]

