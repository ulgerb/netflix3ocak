from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile


def profileUser(request):
   profile_list = Profile.objects.filter(user=request.user)
   
   if request.method == "POST":
      submit = request.POST.get("submit")
      
      if submit == "profileCreate":
         # Profil Ekleme Start
         if len(profile_list) < 4:
            pname = request.POST.get("pname")
            image = request.FILES.get("image")
            
            # if pname.strip(" ") == "" or profile_list.filter(name=pname).exists():
            #    messages.warning(request, "Profile adını giriniz yada değiştiriniz!!")
            #    return redirect("profileUser")
            
            profile = Profile(name=pname, image=image, user=request.user)
            if image is None:
               profile.image = "profile/smile-icon.jpg"
            
            profile.save()
            
         else:
            messages.warning(request, "Maximum profil sayısına ulaştınız!")      
         # Profil Ekleme End
         
         # Profile Düzenleme Start
      elif submit == "profileChange":
         pname2 = request.POST.get("pname2")
         image2 = request.FILES.get("image2")
         pid = request.POST.get("id")
         
         profile2 = profile_list.get(id=pid)
         profile2.name = pname2
         if image2 is not None:
            profile2.image = image2
         profile2.save()
      
         # Profile Düzenleme End
      return redirect("profileUser")
   
   context = {
       "profile_list": profile_list,
   }
   return render(request, 'browse.html',context)

def accountUser(request):
   context = {}
   return render(request, 'hesap.html',context)

def loginUser(request):
   context = {}
   if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      
      user = authenticate(username=username, password=password) # kullanıcı varsa kullanıcı adını yoksa None değeri döndürür
      # if user != None:
      if user is not None:
         login(request, user)
         return redirect('profileUser')
      else:
         # context.update({"hata":"kullanıcı adı veya şifre yanlış!"})
         messages.warning(request, "Kullanıcı adı veya şifre yanlış!")
         return redirect('loginUser')      
      
   
   return render(request, 'login.html',context)
   
def registerUser(request):
   context = {}
   # Kullanıcı önerme eklenicek
   
   if request.method == "POST":
      fname = request.POST.get("fname")
      lname = request.POST.get("lname")
      email = request.POST.get("email")
      username = request.POST.get("username")
      password1 = request.POST.get("password1")
      password2 = request.POST.get("password2")
      
      password_bool = email_bool = username_bool = True 
      if password1 != password2:
         password_bool = False
         messages.warning(request, "Şifreler aynı değil!")
      if User.objects.filter(username=username).exists(): # exists list içinde obje varsa True yoksa False döndürür
         username_bool = False
         messages.warning(request, "Bu kullanıcı adı zaten kullanılıyor!")
      if User.objects.filter(email=email).exists(): # exists liste içerisi boşsa None döndürür
         email_bool = False
         messages.warning(request, "bu email zaten başkası tarafından kullanılmış!")
         
      if password_bool and email_bool and username_bool:
         user = User.objects.create_user(first_name = fname, last_name=lname, email=email, username=username, password=password1) # obje oluştur
         user.save() # objeyi yani kullanıcıyı kaydet
         return redirect("loginUser")
      
      
   return render(request, 'register.html',context)


def logoutUser(request):
   logout(request)
   return redirect("indexPage")