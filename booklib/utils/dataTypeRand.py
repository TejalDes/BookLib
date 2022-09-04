#For Reference
#https://www.thepythoncode.com/article/generate-random-data-in-python#generating-random-integers


import random
import string
import datetime
import uuid


  
#*************************NUMBER FIELDS***************************

#return an integer in a range
def randIntField(maxInt=2147483647, mInt=-2147483648):
    if mInt>maxInt:
        randint = random.randint(maxInt,mInt)
    else:
        randint = random.randint(mInt,maxInt)
    return randint

#return a float in a range
def randFloatField(maxFloat=10000, mFloat=0 ):
    if mFloat>maxFloat:
        randfloat = random.uniform(maxFloat, mFloat)
    else:
        randfloat = random.uniform(mFloat, maxFloat)
    return randfloat

# elif type(field) == BigIntegerField:
def randBigIntField(maxBInt=9223372036854775807, mBInt=-9223372036854775808):
    if mBInt>maxBInt:
        randBInt = random.randint(maxBInt,mBInt)
    else:
        randBInt = random.randint(mBInt,maxBInt)
    return randBInt

# elif type(field) == SmallIntegerField:
def randSmallIntField(maxSInt=32767, mSInt= -32768):
    if mSInt>maxSInt:
        randSInt = random.randint(maxSInt,mSInt)
    else:
        randSInt = random.randint(mSInt,maxSInt)
    return randSInt

# elif type(field) == PositiveIntegerField:2147483647
def randPosIntField(maxPosInt=2147483647, mPosInt= 0, **fkwargs):
    maxPosInt = fkwargs.get('maxPosInt', maxPosInt)
    if mPosInt>maxPosInt:
        randPosInt = random.randint(maxPosInt,mPosInt)
    else:
        randPosInt = random.randint(mPosInt,maxPosInt)
    return randPosInt
            
# elif type(field) == PositiveSmallIntegerField:
def randPosSIntField(maxPosSInt=32767, mPosSInt= 0):
    if mPosSInt>maxPosSInt:
        randPosSInt = random.randint(maxPosSInt,mPosSInt)
    else:
        randPosSInt = random.randint(mPosSInt,maxPosSInt)
    return randPosSInt
            
# elif type(field) == PositiveBigIntegerField:
def randPosBIntField(maxPosBInt=9223372036854775807, mPosBInt= 0):
    if mPosBInt>maxPosBInt:
        randPosBInt = random.randint(maxPosBInt,mPosBInt)
    else:
        randPosBInt = random.randint(mPosBInt,maxPosBInt)
    return randPosBInt

#digit 9 formation
def digi9(n):
    num = 0
    for i in range(n):
        num = num + 9*10**i
    return num

# elif type(field) == DecimalField:
def randDecimalField(max_digits = 10, decimal_places = 2):
    return randBigIntField(10**(max_digits-1), digi9(max_digits)) + randIntField(digi9(decimal_places))/10**decimal_places




#*************************STRING FIELDS***************************

#Capital case string field
def randStrField(fstr=25, **fkwargs):
    fstr= randPosIntField(1,fkwargs.get('fstr', fstr))
    print(fstr)
    randstring = ''.join(random.choices(string.ascii_lowercase, k=fstr))
    print(randstring)
    return randstring

#email field
def randEmailField(fEmail=20, **fkwargs):
    txt = randStrField(nstr=fkwargs.get('fEmail',fEmail))
    randemail = txt[:12] + '@' + txt[-5:] + '.com'
    return randemail

#urlField
def randUrlField(fUrl=20, **fkwargs):
    txt = randStrField(fkwargs.get('fUrl',fUrl))
    randurl = 'https://www.' + txt[:10] + '.' + txt[:3]
    return randurl

#add letters to list
def slugLettersToList():
    sluglist = ['_','-']
    sluglist.extend([str(x) for x in range(0,10)])
    sluglist.extend([chr(x) for x in range(ord('a'),ord('z')+1)])
    sluglist.extend([chr(x) for x in range(ord('A'),ord('Z')+1)])
    return sluglist

# elif type(field) == SlugField:
def randSlugField(slug_max_length = 50):
    strSlug = ''
    strSlug = [strSlug + str(randChoiceFromList(slugLettersToList())) for i in range(slug_max_length)]
    return "".join([str(i) for i in strSlug])

# elif type(field) == TextField:
def randTextField(text_max_length = 2500):
    return " ".join(randStrField(randIntField(10)) for i in range(300))


#return a choice of string from a list
def randChoiceFromList(ForeignKeyList):
    choice = random.choice(ForeignKeyList)
    return choice



#*************************BOOLEAN & UUID FIELDS***************************

# elif type(field) == BooleanField:
def randBoolean():
    return random.choice([True, False])

#elif type(field) == UUIDField:
def randUUID():
    return uuid.uuid1()




#*************************DATE FIELDS***************************

# #random Date
def randDateField(mDate=datetime.datetime.now(), **fkwargs):
    mDate = fkwargs.get('mdate', mDate)
    return mDate - datetime.timedelta(randIntField(1,10000))

# # elif type(field) == DateTimeField:
# def randDateTimeField():

# #elif type(field) == TimeField:
# def randTimeField():

# # elif type(field) == DurationField:
# def randTimeField():



            
            # elif type(field) == GenericIPAddressField:..........Is this required?
            
            # elif type(field) == NullBooleanField:...............Is this required?
        
# def StrField(**kwargs):
#     print("strfield",kwargs['nstr'])
#     return kwargs['nstr']*10

# def UrlField(**kwargs):
#     print("urlfield",kwargs['nUrl'])
#     return kwargs['nUrl']+100

            

