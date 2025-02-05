from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('cargo/', views.cargo_view, name='cargo_view'),
    path('cargo/add/', views.cargo_view, name='cargo_view'),
    path('cargo/edit/<int:id>/', views.edit_cargo, name='edit_cargo'),
    path('cargo/delete/<int:id>/', views.delete_cargo, name='delete_cargo'),
]