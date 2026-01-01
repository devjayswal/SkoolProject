
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('skool.urls')),
    path('student/',include('student.urls')),
]
