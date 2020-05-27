from django.contrib import admin
from .models import UserProfile,HomeContents,ImportantLinks,headerimage,NoticeContent,BackToBack2,BookShelf

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(HomeContents)
admin.site.register(ImportantLinks)
admin.site.register(headerimage)
admin.site.register(NoticeContent)
admin.site.register(BackToBack2)
admin.site.register(BookShelf)
