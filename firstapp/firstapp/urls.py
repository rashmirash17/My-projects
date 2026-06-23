from django.contrib import admin
from django.urls import path
from .views import first   # ✅ import your function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first),   # homepage
]