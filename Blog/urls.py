from django.contrib import admin
from django.urls import include 
from django.conf.urls import url
from django.urls import path
from .import views 


urlpatterns = [
    url('admin/', admin.site.urls),
     path('',views.home,name='home'),
    path('event',views.event,name='event'),
    path('notice',views.notice,name='notice'),
    path('login',views.login,name='login'),
    path('about',views.about,name='about'),
    path('Segments',views.Segments,name='Segments'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('Library',views.book,name='book'),
  
   

   
   
  
]
