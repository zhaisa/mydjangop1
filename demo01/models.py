from django.db import models
from django.contrib import admin

# Create your models here.
from django.utils.html import format_html


class Grades(models.Model):
    gname=models.CharField(max_length=20)
    gdate=models.DateField()
    ggirlnum=models.IntegerField()
    gboynum=models.IntegerField()
    isDelete=models.BooleanField(default=False)
    def __str__(self):
        return "%s-%d-%d"%(self.gname,self.gboynum,self.ggirlnum)
class Students(models.Model):
    sname=models.CharField(max_length=20)
    sgender=models.BooleanField(default=True)
    sage=models.IntegerField()
    scontend=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    sgrade=models.ForeignKey("Grades",on_delete=models.CASCADE,)
class Blog(models.Model):
    id=models.IntegerField(primary_key=True)
    caption=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    publish_time=models.DateField()
class Blogcon(models.Model):
    machine_room_id=models.IntegerField(primary_key=True)
    use=models.CharField(max_length=20,verbose_name="用途")
    status=models.CharField(max_length=20,verbose_name="状态")
    head=models.CharField(max_length=20,verbose_name="负责人")
    type=models.CharField(max_length=20,verbose_name="型号")
    memory=models.CharField(max_length=20,verbose_name="内存")
    cpu=models.CharField(max_length=20,verbose_name="cpu")
    cipan=models.CharField(max_length=20,verbose_name="cpu")
    operating=models.CharField(max_length=20,verbose_name="操作系统")
    belonghouse=models.CharField(max_length=20,verbose_name="所属机房")
    belonggroup=models.CharField(max_length=20,verbose_name="所属组")
    sblogs=models.ForeignKey("Blog",on_delete=models.CASCADE,)
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=6)

    def colored_name(self):
        return format_html(
            '<span style="color: #{};">{} {}</span>',
            self.color_code,
            self.first_name,
            self.last_name,
        )


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'colored_name')
class Dreamreal(models.Model):

   website = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   name = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()
   online = models.ForeignKey('Online', default=1,on_delete=models.CASCADE,)
   class Meta:
      db_table = "dreamreal"


class Online(models.Model):
    domain = models.CharField(max_length=30)
    company=models.CharField(max_length=30)


class Meta:
    db_table = "online"