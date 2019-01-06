from django.db import models

# Create your models here.
class Grades(models.Model):
    gname=models.CharField(max_length=20)
    gdate=models.DateField()
    ggirlnum=models.IntegerField()
    gboynum=models.IntegerField()
    isDelete=models.BooleanField(default=False)
class Students(models.Model):
    sname=models.CharField(max_length=20)
    sgender=models.BooleanField(default=True)
    sage=models.IntegerField()
    scontend=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    sgrade=models.ForeignKey("Grades",on_delete=models.CASCADE,)
   # on_delete=models.CASCADE()