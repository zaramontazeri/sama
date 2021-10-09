from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import FileUploadParser,MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status , permissions
from rest_framework.generics import ListAPIView,DestroyAPIView, RetrieveAPIView
from .serializers import ImageSerializer, ImageThumbnailSerializer,FileSerializer,FileDetailSerializer
from .models import Image,File

class ImageUploadView(APIView):
    '''
    "file":file
    "name":char(100)
    "caption":char(100)
    "alt":char(100)
    '''
    parser_class = (FileUploadParser,MultiPartParser)
    permission_classes = [permissions.IsAuthenticated] 
    def post(self, request, *args, **kwargs):
      data = request.data
      data["user"] = request.user.pk
      file_serializer = ImageSerializer(data=data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageListAPIView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    # permission_classes = [permissions.IsAuthenticated] 


class ImageListThumbNailAPIView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageThumbnailSerializer
    # permission_classes = [permissions.IsAuthenticated] 

class ImageDeleteAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated] 
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

class ImageDetailAPIView(RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated] 
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

class ImageUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated] 
    parser_class = (FileUploadParser,MultiPartParser)

    def put(self, request, pk):
        data = request.data
        data["user"] = request.user.pk
        instance = Image.objects.get(pk=pk)
        file_serializer = ImageSerializer(instance , data=data,partial=True)
        
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FileUploadView(APIView):
    '''
    "file":file
    "name":char(100)
    "caption":char(100)
    "alt":char(100)
    '''
    parser_class = (FileUploadParser,MultiPartParser)
    permission_classes = [permissions.IsAuthenticated] 
    def post(self, request, *args, **kwargs):
      data = request.data
      data["user"] = request.user.pk
      file_serializer = FileSerializer(data=data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListAPIView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    # permission_classes = [permissions.IsAuthenticated] 



class FileDeleteAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated] 
    serializer_class = FileSerializer
    queryset = File.objects.all()

class FileDetailAPIView(RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated] 
    serializer_class = FileDetailSerializer
    queryset = File.objects.all()

class FileUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated] 
    parser_class = (FileUploadParser,MultiPartParser)

    def put(self, request, pk):
        data = request.data
        data["user"] = request.user.pk
        instance = File.objects.get(pk=pk)
        file_serializer = FileSerializer(instance , data=data,partial=True)
        
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


