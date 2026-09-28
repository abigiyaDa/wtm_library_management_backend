from django.urls import path
from author.views import author_view

urlpatterns = [
    path('',author_view)
]