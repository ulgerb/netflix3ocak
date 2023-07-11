from django.shortcuts import render


def profileUser(request):
   context = {}
   return render(request, 'browse.html',context)

def accountUser(request):
   context = {}
   return render(request, 'hesap.html',context)

def loginUser(request):

   if request.method == "POST":
      print(request.POST)
   
   context = {}
   return render(request, 'login.html',context)
   
def registerUser(request):
   context = {}
   return render(request, 'register.html',context)