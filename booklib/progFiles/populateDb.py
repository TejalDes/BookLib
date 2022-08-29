#Reference from
#https://stackoverflow.com/questions/11637293/iterate-over-object-attributes-in-python

""""
import dataTypeRand.py

def populateDbase(obj_instance):
    fieldList = [a for a in dir(obj_instance) if not a.startswith('__')]
    for field in fieldList:
        if type(field) == 'int':
            #call randint function to assign to this field of obj instance
        elif type(field) == 'float':
            #call randfloat function to assign to this field of obj instance
        elif type(field) == 'string':
            #call randstr function to assign to this field of obj instance
        elif type(field) == 'date':
            #call randdate function to assign to this field of obj instance
        elif type(field) == 'email':
            #call randemail function to assign to this field of obj instance
        elif type(field) == 'url':
            #call randurl function to assign to this field of obj instance
        else:
            #assign null to this field of obj  if null is allowed

"""

#make a string of assigning data to instance
#find how to run that string in the shell
#take care of the foreign keys while populating child table
