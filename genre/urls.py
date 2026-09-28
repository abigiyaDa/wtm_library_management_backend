from django.urls import path
from genre.views import genre 

urlpatterns=[
    path('',genre)
]