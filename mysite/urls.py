from django.contrib import admin
from django.urls import path
from stone_scissors import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first),
    path('choice', views.my_choise)
]