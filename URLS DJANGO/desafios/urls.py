from django.urls import path
from .views import domingo, segunda, terca
urlpatterns = [
    path('domingo', domingo),
    path('segunda', segunda),
    path('terca', terca)
]
