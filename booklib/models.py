from django.db import models
from django.db.models.fields import *
from booklib.progFiles.dataTypeRand import *
from django.db.models.fields.related  import *

class Author(models.Model):
    author_name = models.CharField(max_length =255)
    author_email = models.EmailField(max_length=255)

    def __str__(self):
        return self.author_name
    
    def randomData(self):
        fieldset = self._meta.fields
        dataDict ={}
        for field in fieldset:
            if type(field) == BigAutoField or type(field) == AutoField:
                continue
            
            elif type(field) == CharField:
                dataDict[field.attname] = randStrField()
                
            elif type(field) == DateField:
                dataDict[field.attname] = randPastDateField()
            
            elif type(field) == EmailField:
                dataDict[field.attname] = randEmailField()
            
            elif type(field) == URLField:
                dataDict[field.attname] = randUrlField()
            
            elif type(field) == ForeignKey:
                #generic
                dataDict[field.attname] = field.related_model.randomObject()

        return(dataDict)

            
            # elif type(field) == BigIntegerField:
            
            # elif type(field) == BinaryField:
            
            # elif type(field) == BooleanField:
            
            # elif type(field) == DateTimeField:
            
            # elif type(field) == DecimalField:
            
            # elif type(field) == DurationField:
            
            # elif type(field) == FileField:
            
            # elif type(field) == FloatField:
            
            # elif type(field) == ImageField:
            
            # elif type(field) == IntegerField:
            
            # elif type(field) == GenericIPAddressField:
            
            # elif type(field) == NullBooleanField:
            
            # elif type(field) == PositiveIntegerField:
            
            # elif type(field) == PositiveSmallIntegerField:
            
            # elif type(field) == PositiveBigIntegerField:
            
            # elif type(field) == SlugField:
            
            # elif type(field) == SmallIntegerField:
            
            # elif type(field) == TextField:
            
            #elif type(field) == TimeField:
            
            #elif type(field) == UUIDField:
            
            #else:
            #assign null to this field of obj  if null is allowed

    @staticmethod
    def randomObject():
        randObjList = Author.objects.all()
        idList =[]
        for i in randObjList: 
            idList.append(i.id)
            print(idList)
        return randChoiceFromList(idList)

        
    


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=255)
    publisher_email = models.EmailField(max_length=255)
    publisher_site = models.URLField(max_length=255)

    def __str__(self):
        return self.publisher_name
    
    def randomData(self):
        fieldset = self._meta.fields
        dataDict ={}
        for field in fieldset:
            if type(field) == BigAutoField or type(field) == AutoField:
                continue
            
            elif type(field) == CharField:
                dataDict[field.attname] = randStrField()
                
            elif type(field) == DateField:
                dataDict[field.attname] = randPastDateField()
            
            elif type(field) == EmailField:
                dataDict[field.attname] = randEmailField()
            
            elif type(field) == URLField:
                dataDict[field.attname] = randUrlField()
            
            elif type(field) == ForeignKey:
                #generic
                dataDict[field.attname] = field.related_model.randomObject()

        return(dataDict)


    @staticmethod
    def randomObject():
        randObjList = Publisher.objects.all()
        idList =[]
        for i in randObjList: 
            idList.append(i.id)
        return randChoiceFromList(idList)

class Books(models.Model):
    book_name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_price = models.IntegerField()
    book_isbn = models.CharField(max_length=255)
    book_published_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("book_name", "author", "book_isbn")
    
    def __str__(self):
        return self.book_name
    
    def randomData(self):
        fieldset = self._meta.fields
        dataDict ={}
        for field in fieldset:
            if type(field) == BigAutoField or type(field) == AutoField:
                continue
            
            elif type(field) == CharField:
                dataDict[field.attname] = randStrField()
                
            elif type(field) == DateField:
                dataDict[field.attname] = randPastDateField()
            
            elif type(field) == EmailField:
                dataDict[field.attname] = randEmailField()
            
            elif type(field) == URLField:
                dataDict[field.attname] = randUrlField()
            
            elif type(field) == ForeignKey:
                #generic
                dataDict[field.attname] = field.related_model.randomObject()

        return(dataDict)




