"""University_Campus_Online_Automation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:

    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('student/', include('Student.urls')),
    path('accounts/', include('accounts.urls')),
    path('', views.home_page,name="home"),
    path('', views.home_page,name="home"),
path('dashboard/', views.dashboard,name="dashboard"),
path('dashboard/studentdetail', views.studentdetail,name="studentdetail"),
path('dashboard/feedetail', views.feedetail,name="feedetail"),
path('dashboard/drivedetail', views.drivedetail,name="drivedetail"),

]

urlpatterns += staticfiles_urlpatterns()
