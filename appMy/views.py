from django.shortcuts import render, get_object_or_404
from appUser.models import Profile  


def indexPage(request):
   context = {}
   return render(request, 'index.html',context)


def netflixPage(request,id):
   profile = get_object_or_404(Profile, id=id)
   
   context = {
      "profile": profile,
   }
   return render(request, 'browse-index.html',context)


