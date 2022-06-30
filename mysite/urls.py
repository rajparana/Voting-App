from django.urls import re_path, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
                re_path('admin/', admin.site.urls),
                re_path('', include('polls.urls')),
               ]
