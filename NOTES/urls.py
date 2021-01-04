from django.urls import path
from .views import BooksSerializerView

urlpatterns = [
    path('books/', BooksSerializerView.as_view()),
]