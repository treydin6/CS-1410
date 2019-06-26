# These drills gave us a Pencil class listed below
MAX_LEAD_LENGTH = 10
MAX_NUM_LEADS = 5

class Pencil:

    def __init__(self, num_leads):
        self.mNumLeads = 0
        self.mCurrentLeadLength = MAX_LEAD_LENGTH
        self.addLeads(num_leads)
        return

    def getNumLeads(self):
        return self.mNumLeads

    def getCurrentLeadLength(self):
        return self.mCurrentLeadLength

    def click(self):
        if self.mCurrentLeadLength > 0:
            self.mCurrentLeadLength -= 1
        if self.mCurrentLeadLength == 0 and self.mNumLeads > 0:
            self.mCurrentLeadLength = MAX_LEAD_LENGTH
            self.mNumLeads -= 1
        return self.mCurrentLeadLength > 0

    def addLeads(self, num_additional_leads):
        if num_additional_leads > 0:
            self.mNumLeads += num_additional_leads
            if self.mNumLeads > MAX_NUM_LEADS:
                self.mNumLeads = MAX_NUM_LEADS
        return self.mNumLeads

# drill 1
# in this exercise, you will create a function that receives no parameters and returns a Pencil object constructed with 3 leads.
from Pencil import *
def create01():
    return Pencil(3)

# dril 2
# In this exercise, you will create a function that receives a Pencil object as a parameter. It will return the length of the current lead in the pencil.
from Pencil import *
def query01(pencil):
    return pencil.getCurrentLeadLength()

# drill 3
# In this exercise, you will create a function that receives a Pencil object as a parameter. It will click the pencil 13 times, and return the pencil.
from Pencil import *
def modify01(pencil):
    for i in range(13):
        pencil.click()
    return pencil

# drill 4
# In this exercise, you will create a function that receives no parameters and returns a Pencil object constructed with 10 leads.
from Pencil import *
def create02():
    return Pencil(10)

# drill 5
# In this exercise, you will create a function that receives a Pencil object as a parameter. It will return the number of leads in the pencil.
def query02(pencil):
    return pencil.getNumLeads()

# drill 6
# In this exercise, you will create a function that receives a Pencil object as a parameter. It will add 2 leads to the pencil, then return the pencil.
def modify02(pencil):
    pencil.addLeads(2)
    return pencil

# drill 7
# In this exercise, you will create a function that receives one integer parameter and returns a Pencil object constructed with the number of leads specified by the parameter.
from Pencil import *
def create03(num_leads):
    return Pencil(num_leads)

# drill 8
# In this exercise, you will create a function that receives a Pencil object as a parameter. It will return the total length of lead in the pencil. This includes the current lead length, and the full length of all other leads.
def query03(pencil):
    b = pencil.getCurrentLeadLength()
    a = pencil.getNumLeads()
    return b +(a * 10)

# drill 9
# In this exercise, you will create a function that receives a Pencil object as a parameter. It will click the pencil 53 times. Then, it will add 2 leads. Finally, it will click the pencil 13 more times. At the end it will return the pencil.
def modify03(pencil):
    p = pencil
    for i in range(53):
        p.click()
    p.addLeads(2)
    for i in range(13):
        p.click()
    return p

# drill 10
# In this exercise, you will create a function that receives a Pencil object as a parameter. It will click the pencil until the current lead length is at the maximum possible value. The pencil will always have enough lead for this to work. At the end it will return the pencil
def modify04(pencil):
    while pencil.getCurrentLeadLength() != 10:
        pencil.click()
    return pencil
