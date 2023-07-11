from django.shortcuts import render



def indexPage(request):
   context = {}
   return render(request, 'index.html',context)

def browsePage(request):
   context = {}
   return render(request, 'browse-index.html',context)

def profileUser(request):
   context = {}
   return render(request, 'browse.html',context)

def accountUser(request):
   context = {}
   return render(request, 'hesap.html',context)

def loginUser(request):
   context = {}
   return render(request, 'login.html',context)
