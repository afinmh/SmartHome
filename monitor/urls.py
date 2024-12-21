from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_status/<str:group>/', views.get_status, name='get_status'),
    path('update_status/<str:group>/', views.update_status, name='update_status'),
]

