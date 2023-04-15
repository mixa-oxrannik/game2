from django.contrib import admin
from django.urls import path
from stone_scissors import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.result_game),
    path('choice', views.my_choise)
]
