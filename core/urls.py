from django.urls import path
from .views import index, contact, company

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('company/', company, name='company'),
]