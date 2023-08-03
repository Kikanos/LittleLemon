#update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('Restaurant.urls')),
]
