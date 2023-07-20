from django.shortcuts import render, get_object_or_404
from appUser.models import Profile  


def indexPage(request):
   context = {}
   return render(request, 'index.html',context)


# def netflixPage(request,id): # url yönlendirmeli
#    profile = get_object_or_404(Profile, id=id)
   
#    context = {
#       "profile": profile,
#    }
#    return render(request, 'browse-index.html',context)

def netflix(request): # form loginp = True yönlendirmeli
   profile = Profile.objects.filter(loginp=True, user=request.user).first()
   context = {
      "profile": profile,
   }
   return render(request, 'browse-index.html',context)
   

