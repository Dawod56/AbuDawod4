from django.db import models
from django.db.models import Model 
# Create your models here.
class Registration(models.Model):
    userName= models.CharField(max_length=100)
    password= models.CharField(max_length=20)
    

class UserProfile(models.Model):
    UserName=models.CharField(max_length=100)
    PhoneNumber=models.IntegerField()
    email = models.EmailField(max_length=200)
    Description = models.CharField(max_length=1000)
    UserImage = models.ImageField(upload_to='pics', blank=True)
    def __str__(self):
        return self.UserName

class HomeContents(models.Model):
    time = models.DateField(auto_now_add=True)
    PostTitle = models.CharField(max_length=200)
    PostImage =  models.ImageField(upload_to='HomePostPics', blank=True)
    Description = models.CharField(max_length=10000)
    def __str__(self):
        return self.PostTitle

class ImportantLinks(models.Model):
    LinkName = models.CharField(max_length=200)
    Link = models.URLField(max_length=200)
   
    def __str__(self):
        return self.LinkName

class headerimage(models.Model):
    img=models.ImageField(upload_to='headers', blank=True)
    Tag=models.CharField(max_length=100)
    def __str__(self):
        return self.Tag

class NoticeContent(models.Model):
    NoticeImage = models.ImageField(upload_to='Notice', blank=True)
    NoticeTitle = models.CharField(max_length=200)
    NoticeDescription = models.CharField(max_length=200)
    NoticeDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.NoticeTitle

class BackToBack(models.Model):
    BackDate= models.DateField(auto_now_add=True)
    BackIntro=models.CharField(max_length=500,blank=True)
    BackDescription=models.CharField(max_length=2000)
    BackUser=models.CharField(max_length=200,blank=True)
    BackUserDiscipline =models.CharField(max_length=200,blank=True)
    BackUniversity = models.CharField(max_length=100,blank=True)
    
    def __str__(self):
        return self.BackDate 

class BackToBack2(models.Model):
    BackDate= models.DateField(auto_now_add=True)
    BackIntro=models.CharField(max_length=500,blank=True)
    BackDescription=models.CharField(max_length=2000)
    BackUser=models.CharField(max_length=200,blank=True)
    BackUserDiscipline =models.CharField(max_length=200,blank=True)
    BackUniversity = models.CharField(max_length=100,blank=True)
    BackVisibility =models.BooleanField(default=False)
    def __str__(self):
        return self.BackUser

class BookShelf(models.Model):
    BookName = models.CharField(max_length=500)
    Writer = models.CharField(max_length=500,blank=True)
    BookLink = models.URLField(max_length=2000)
    BookCategory = models.CharField(max_length=500,blank=True)
    def __str__(self):
        return self.BookName