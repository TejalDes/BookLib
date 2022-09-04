#Important : Remember to call this function on the primary models before calling it on the secodary ones with foreign keys
from django.db.models.fields import *
from booklib.utils.dataTypeRand import *
from django.db.models.fields.related  import *

fieldTypeDict = {
    CharField : randStrField, #nstr
    IntegerField : randPosIntField, #maxPosInt 
    DateField : randDateField, 
    EmailField : randEmailField, #nEmail
    URLField : randUrlField, #nUrl
    BooleanField : randBoolean, 
    UUIDField : randUUID 
}


def randomData(modelClass, n=1, **kwargs):
    recordsList = []
    dataDict ={}
    for i in range(n):
        dataDict.clear()
        for field in modelClass._meta.fields:
            if type(field) == BigAutoField or type(field) == AutoField:
                continue
            elif type(field) == ForeignKey:
                dataDict[field.attname] = None
            else:
                dataDict[field.attname] = fieldTypeDict[type(field)](fstr=kwargs.get('nstr', field.max_length), fEmail=kwargs.get('nEmail',field.max_length), fUrl=kwargs.get('nUrl', field.max_length), maxPosInt = kwargs.get('maxPosInt',5000), mDate = kwargs.get('mDate', datetime.datetime.now()))
        tempDict = dataDict.copy()
        recordsList.append(tempDict)
    return(recordsList)


        
    # @staticmethod
    # def randomObject():
    #     randObjList = Author.objects.all()
    #     idList =[]
    #     for i in randObjList: 
    #         idList.append(i.id)
    #         print(idList)
    #     return randChoiceFromList(idList)
