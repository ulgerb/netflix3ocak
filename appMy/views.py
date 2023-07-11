from django.shortcuts import render



def indexPage(request):
   context = {}
   return render(request, 'index.html',context)

def browsePage(request):
   context = {}
   return render(request, 'browse-index.html',context)


