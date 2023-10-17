from django.shortcuts import render

# Create your views here.
from .serializers import *
from rest_framework.views import APIView
from rest_framework import status, response
from rest_framework.response import Response
from .models import Book

class Books(APIView):
    serialiser_class = BookSerializer
    def post(self,request):
        serializer = self.serialiser_class(data = request.data)
        if serializer .is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def get(self,request,id=None):
        
        if id:
            bookid=Book.objects.get(pk=id)
            serializer = BookSerializer(bookid)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        bookdata = Book.objects.all()
        serializer = BookSerializer(bookdata, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self,request,id):
        bookid=Book.objects.get(pk=id)
        serializer = BookSerializer(bookid,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "update successfully", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
        
    def delete(self,request,id):
        bookid=Book.objects.get(pk=id)
        bookid.delete()
        return Response({"status": "success", "data": "delete successfully"})
