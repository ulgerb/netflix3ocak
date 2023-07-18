from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı Adı"), on_delete=models.CASCADE)
   name = models.CharField(("Profil Adı"), max_length=50)
   image = models.ImageField(("Profil Resmi"), upload_to='profile', max_length=200)
   
   
   def __str__(self) -> str:
      return self.user.username
   

