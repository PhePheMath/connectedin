from django.urls import path

from . import views

app_name = 'perfil'

urlpatterns = [
    path('', views.home_page, name='profile'),
    path('<str:username>', views.contact_page, name='contact'),
    path('register/', views.register, name='register'),
    path('invite/<str:contact>', views.invite, name='invite'),
]
