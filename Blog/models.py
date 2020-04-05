from django.db import models


# Create your models here.
class Creator(models.Model):
    name = models.CharField(max_length=200)
    join_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Post(models.Model):
    creator = models.ForeignKey(Creator, max_length=150,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500,default="Lets come and read")
    image = models.ImageField(default='default.jpg',upload_to='media/')
    content = models.TextField()
    def __str__(self):
        return self.title