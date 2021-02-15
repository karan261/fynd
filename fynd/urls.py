"""fynd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls.conf import include
from movie_rating import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()                                  # router is used for declare all seprate routes into single route.

router.register('movieapi',views.MovieViewSet,basename='movie')

urlpatterns = [
    path('admin/', admin.site.urls),                    # urlpattern is used for maps a set of requested URL given inside in urlpattern to the correct views in your views.py file
    path('',include(router.urls))
]
