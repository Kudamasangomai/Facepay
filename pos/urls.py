from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('billing/', views.billing, name='billing'),
    path('billing/order', views.order, name='order'),
    path('login/', views.User_login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('search_username',views.search_username,name='search-username')
]
