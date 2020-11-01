from django.urls import path

from . import views

app_name = 'timeline'

urlpatterns = [
    path('', views.post, name='post'),
    path('timeline/', views.timeline, name='timeline'),
]
