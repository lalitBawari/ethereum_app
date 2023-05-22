from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('balance', include('balance.urls')),
    path('admin/', admin.site.urls),
]
