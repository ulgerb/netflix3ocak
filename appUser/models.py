from django.db import models
from django.contrib.auth.models import User


class Userinfo(models.Model):
   user = models.OneToOneField(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   password = models.CharField(("Kullanıcı Şifresi"), max_length=50)
   tel = models.CharField(("Telefon"), max_length=50, default="-")

   def __str__(self) -> str:
      return self.user.username
   
class Profile(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı Adı"), on_delete=models.CASCADE)
   name = models.CharField(("Profil Adı"), max_length=50)
   image = models.ImageField(("Profil Resmi"), upload_to='profile', max_length=200)
   loginp = models.BooleanField(("Girişli Profile"), default=False)
   
   def __str__(self) -> str:
      return self.user.username
   

