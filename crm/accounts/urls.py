from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<int:pk>/', views.customer, name="customer"),
    path('create_order/<int:pk>/', views.create_order, name="create_order"),
    path('update_order/<int:pk>/', views.update_order, name="update_order"),
    path('delete_order/<int:pk>/', views.delete_order, 
    name="delete_order"),

    path('login/', views.loginPage, name='login'),
    path('register/', views.registrePage, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    path('user/', views.userPage, name='user-page'),
    path('account/', views.accountSettings, name='account')
]