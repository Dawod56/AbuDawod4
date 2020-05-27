from django.contrib import admin
from django.urls import include 
from django.conf.urls import url
from django.urls import path
from .import views 


urlpatterns = [
    url('admin/', admin.site.urls),
  
    path('IT',views.IT,name='IT'),
    path('Language',views.language,name='language'),
    path('Scholars',views.Scholar,name='Scholar'),
    path('Govornor',views.gov,name='gov'),
   

   
   
  
]
