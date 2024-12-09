from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('login/', views.user_login, name='logins'),
    path('detail/<int:human_id>/', views.user_detail, name='details'),
    path('delete/<int:human_id>/', views.user_delete, name='delete'),
    path('edit/<int:human_id>/', views.user_edit, name='edit'),
    path('register/', views.user_register, name='register'),
]
