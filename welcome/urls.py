from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send_email/', views.send_email, name='send_email'),
    path('discover_more/', views.discover_more, name='discover_more'),
    path('send-newsletter/', views.send_newsletter_email, name='send_newsletter_email'),

]
