from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_customers, name='customer_reg'),
    path('register_face/', views.register_face, name='face_url'),
    path('thanks_sms/', views.thank_page, name='thank_sms')
]
#name='reguser'