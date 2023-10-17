from .models import Book
from django.test import TestCase
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.test import APIClient

class BooksAPITest(TestCase):
    def setUp(self):
        Book.objects.create(
            title="Book",
            author="Author",
            publication_year=2023
        )

    def test_post_method(self):
        url = "http://127.0.0.1:8000/api/books/"

        data = {
            "title": "Book",
            "author": "Author",
            "publication_year": 2023
        }
        
        response = self.client.post(url, data, format='json')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_method(self):
        url = "http://127.0.0.1:8000/api/books/"
        response = self.client.get(url,format='json')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_method_id(self):
        url = "http://127.0.0.1:8000/api/books/1/"
        response = self.client.get(url,format='json')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_put_method(self):
        url = "http://127.0.0.1:8000/api/books/1/"

        data = {
            "title": "Updated Book",
            "author": "Updated Author",
            "publication_year": 2024
        }

        
        response = self.client.put(url, data, format='json', content_type='application/json')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_method(self):
        url = "http://127.0.0.1:8000/api/books/1/"
        response = self.client.delete(url, format='json', content_type='application/json')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)