from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("moblie/",include("mobile.urls")),
    path("laptop/",include("lapytop.urls"))
]