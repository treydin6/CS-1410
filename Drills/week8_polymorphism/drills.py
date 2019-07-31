# drill 1
# init method
class MathProblem:
    def __init__(self, lhs, rhs):
        self.mLHS = lhs
        self.mRHS = rhs
        self.operator = ''

# drill 2
# getter methods
def getLHS(self):
        return self.mLHS

def getRHS(self):
    return self.mRHS

def getOperator(self):
    return self.operator

# drill 3
# True if a change occurred, False otherwise.
def setLHS(self, value):
        if self.getLHS() != value:
            self.mLHS = value
            return True
        else:
            return False

def setRHS(self, value):
    if self.getRHS() != value:
        self.mRHS = value
        return True
    else:
        return False

def setOperator(self, value):
    if value == '+' or value == '-' or value == '*' or value == '/':
        self.operator = value
        return True
    else:
        return False

# drill 4
# 
def getString(self):
        return ''
    
def checkAnswer(self, ans):
    if ans == (self.getLHS() + self.getRHS()):
        return True
    else:
        return False

# drill 5
# Uses constructor chaining to initialize the MathProblem portions of the class. 
# Then, use the method from MathProblem to set the operator to the string "+".
import mathproblem
class AdditionProblem(mathproblem.MathProblem):
    def __init__(self, lhs, rhs):
        super().__init__(lhs, rhs)
        self.operator = '+'

# drill 6
# A string that represents the values of this problem. For example, "2 + 5".
# True if ans is correct, False otherwise.
def getString(self):
        new_str = str(self.mLHS) + " + " + str(self.mRHS)
        return new_str

def checkAnswer(self, ans):
    correct_answer = self.mLHS + self.mRHS
    if ans == correct_answer:
        return True
    else:
        return False

# drill 7
#  init method, same as addition
import mathproblem
class MultiplicationProblem(mathproblem.MathProblem):
    def __init__(self, lhs, rhs):
        super().__init__(lhs, rhs)
        self.operator = '*'

# drill 8
# A string that represents the values of this problem. For example, "2 * 5".
def getString(self):
        new_str = str(self.mLHS) + " * " + str(self.mRHS)
        return new_str

def checkAnswer(self, ans):
    if ans == (self.mLHS * self.mRHS):
        return True
    else:
        return False

# drill 9
# A list of num_problem problems.
import random
import additionproblem, multiplicationproblem

def make_problems(min_value, max_value, num_problem):
    problems = []
    print('numProb', num_problem)
    for i in range(num_problem):
        rando = random.randrange(1,3)
        lhsRando = random.randrange(min_value, max_value+1)
        rhsRando = random.randrange(min_value, max_value+1)
        if rando == 1:
            a = additionproblem.AdditionProblem(lhsRando, rhsRando)
            a.getString()
            problems.append(a)
        if rando == 2:
            a = multiplicationproblem.MultiplicationProblem(lhsRando, rhsRando)
            a.getString()
            problems.append(a)

    return problems

# drill 10
# A number, the number of answers that were correct.
def check_problems(problems, answers):
    correct_count = 0
    for i in problems:
        if problem[i].CheckAnswer == answers[i]:
            correct_count += 1
    return correct_count

