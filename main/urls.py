from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.get, name='get'),
    path('create/', views.create, name='create'),
]
