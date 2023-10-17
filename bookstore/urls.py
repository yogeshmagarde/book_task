from . import views
from .views import *
from django.urls import path
urlpatterns = [
    path('books/', Books.as_view()),
    path('books/<int:id>/', Books.as_view()),
    
]
