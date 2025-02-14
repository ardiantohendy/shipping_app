from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('cargo/add/logout', views.logout, name='logout'),
    path('cargo/', views.check_cargo, name='check_cargo'),
    path('cargo/add/', views.add_cargo, name='add_cargo'),
    path('cargo/edit/<int:id>/', views.edit_cargo, name='edit_cargo'),
    path('cargo/delete/<int:id>/', views.delete_cargo, name='delete_cargo'),
]