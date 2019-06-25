# drill 1
# In this exercise, your function will receive two numeric parameters. It will return the largest of the sum of the parameters and the product of the parameters.
def biggest02(x, y):
    Sum = x + y
    Product = x * y
    return max(Sum, Product)

# drill 2
# In this exercise your function will receive two parameters: a string(long_word) and a character(char). Use a while loop to go through all the letters in the string and build a new string made up from those letters until you find the char. You may assume that each string will contain the passed in character(char).
def letters_up_to_char(long_word, char):
    new = ''
    for i in range(len(long_word)):
        if long_word[i] == char:
            break
        else:
            new += long_word[i]
    return new

# drill 3
# In this exercise your function will receive two parameters, and return a random number between x and y inclusive.
import random
def randRangeParam2(x, y):
    return random.randrange(x,y+1)

# drill 4
# In this exercise your function will receive three parameters, a list of integers, and two integers. It will add up all values in the list that do not equal either of the two integers.
def suminout(nums, a, b):
    total = 0
    for i in range(len(nums)):
        if nums[i] != a and nums[i] != b:
            total += nums[i]
    return total

# drill 5
# In this exercise, your function will receive 2 parameters, the name of a text file, and a list of strings. The function will write one line to the text file. The line will contain the fourth character of every string in the list. For any strings that don't have four characters, use x. Be sure to include the newline character at the end. 
def fourthchar(filename, lines):
    list = ''
    fin = open(filename, 'w')
    for line in lines:
        if len(line) > 3:
            list += str(line[3])
        else:
             list += 'x'
    print(list)
    fin.write(list + '\n')
    fin.close()

# drill 6
# In this exercise, your function will receive 1 parameter, the name of a text file. The function will return a string created by concatenating the fifth character from each line into one string. If the line has fewer than 5 characters, then the line should be skipped. All lines should have leading and trailing whitespace removed before looking for the fifth character.
def fifthchar(filename):
    new = ''
    fin = open(filename, 'r')
    for line in fin:
        line = line.strip()
        if len(line) > 4:
            new += line[4]
    return new

# drill 7
# def sum13(nums):
  if len(nums) == 0:
    return 0

  for i in range(0, len(nums)):
    if nums[i] == 13:
      nums[i] = 0
      if i+1 < len(nums):
        nums[i+1] = 0
  return sum(nums)

# drill 8
#Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
def combo_string(a, b):
    new = ''
    if len(a) > len(b):
        new += b + a + b
    else:
        new+=a+b+a
    return new

# drill 9
#In this exercise, your function will receive two parameters. The first is a string, and the second is an index into the string. The function returns a copy of the string without the character at the index specified.
def missing_char(string, index):
    return string[:index] + string[index+1:]

# drill 10
#In this exercise, your function will receive two numeric parameters. It will return the largest of the sum of the parameters and the product of the parameters.
def biggest02(x, y):
    Sum = x + y
    Product = x * y
    return max(Sum, Product)
