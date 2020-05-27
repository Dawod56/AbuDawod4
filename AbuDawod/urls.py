from django.contrib import admin
from django.urls import include 
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),
    path('', include("Blog.urls")), 
    path('Segments/', include("Segments.urls")), 
   
  
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
