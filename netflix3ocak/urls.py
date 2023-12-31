"""netflix3ocak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appMy.views import *
from appUser.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexPage,name='indexPage'),
    path('netflix', netflix, name='netflix'),
    # path('netflixPage<id>', netflixPage, name='netflixPage'),
    # === USER ===
    path('subscribeUser', subscribeUser, name='subscribeUser'),
    path('profileUser', profileUser,name='profileUser'),
    # path('deleteProfileUser<id>', deleteProfileUser, name='deleteProfileUser'), # profile silme
    path('accountUser', accountUser,name='accountUser'),
    path('login',loginUser ,name='loginUser'),
    path('register',registerUser ,name='registerUser'),
    path('logout',logoutUser ,name='logoutUser'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
