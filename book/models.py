from django.db import models
from email.policy import default
from random import choices
from book.manager import CustomModelManager

BOOK_CHOICE=(( 
                ('Non-Fiction','Non-Fiction'),
                ('Edited','Edited') ,
                ('Fiction','Fiction'),
                ('Reference','Reference')

    ))
# Create your models here.
class Field(models.Model):
    Book_Name=models.CharField(max_length=30)
    Author_Name=models.CharField(max_length=30)
    Price=models.IntegerField()
    Book_Type=models.CharField(choices=BOOK_CHOICE,max_length=20)
    Is_Deleted=models.CharField(max_length=5,default='n')

    objects=CustomModelManager()
    customManager=CustomModelManager()