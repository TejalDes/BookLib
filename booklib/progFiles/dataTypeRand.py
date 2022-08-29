#For Reference
#https://www.thepythoncode.com/article/generate-random-data-in-python#generating-random-integers


import random
import string
import datetime

#return an integer in a range
def randIntField():
    randint = random.randint(300, 500)
    return randint

def randIntRangeField(m,n):
    randint = random.randint(m, n)
    return randint

#return a float in a range
def randFloatField():
    randfloat = random.uniform(5,10)
    return randfloat

#randomPastDate
def randPastDateField():
    x = datetime.datetime.now()
    return x - datetime.timedelta(randIntRangeField(1,10000))

#random Future date
def randPastDateField():
    x = datetime.datetime.now()
    return x - datetime.timedelta(randIntRangeField(1,10000))

#capitalised string field
def caprandStrField():
    randstring = ''.join(random.sample(string.ascii_lowercase, 15))
    print(randstring.capitalize())

#small case string field
def randStrField():
    randstring = ''.join(random.sample(string.ascii_lowercase, 15))
    return randstring

#emailfield
def randEmailField():
    txt = randStrField()
    randemail = txt[:10] + '@' + txt[-5:] + '.com'
    return randemail

#urlField
def randUrlField():
    txt = randStrField()
    randurl = 'https://www.' + txt[:10] + '.com'
    return randurl


#return a choice of string from a list
def randChoiceFromList(ForeignKeyList):
    choice = random.choice(ForeignKeyList)
    return choice
