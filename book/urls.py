from django.urls import path
from book.views import book

urlpatterns = [
    path('',book)
]