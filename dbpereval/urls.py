from django.urls import path
from .views import *

urlpatterns = [
   path('submitData/', PerevalView.as_view()),
]
