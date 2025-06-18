from django.urls import path
from .views import *

urlpatterns = [
    path('hello', hello),
    path('signup/', signup),
    path('login/', login),
]