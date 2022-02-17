from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='manga-index'),
    path('show/', views.show, name='manga-show'),
    path('new/', views.createManga, name='manga-new'),
    path('about/', views.about, name='manga-about')
]