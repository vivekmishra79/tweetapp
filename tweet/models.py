from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=240)
    photo=models.ImageField(upload_to='photos\it-educational-services-1698228802-7144384.jpgphotos/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}-{self.text[:10]}'