from django.shortcuts import render, get_object_or_404
from watchlist_app.models import WatchList, StreamPlatform, Review

from django.http import JsonResponse
from watchlist_app.api.serializers import (WatchListSerializer, 
                                           StreamPlatformSerializer, 
                                           ReviewSerializer)
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
#from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets


class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
            
# class StreamPlatformVS(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self, request, pk):
#         try:
#             platform = StreamPlatform.objects.get(pk=pk)
#         except:
#             return Response({'error':'Platform not found'},status=status.HTTP_404_NOT_FOUND)
#         platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

            

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        serializer.save(watchlist=watchlist)
        
class ReviewList(generics.ListCreateAPIView):
    #queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class WatchListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchDetailAV(APIView):

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except:
            return Response({'error':'movie not found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except:
            return Response({'error':'movie not found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except:
            return Response({'error':'movie not found'},status=status.HTTP_404_NOT_FOUND)
       
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StreamPlatformAV(APIView):
    
    def get(self, request):
        platform  = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True) #, context={'request':request}
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class StreamDetailAV(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except:
            return Response({'error':'Platform not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except:
            Response({'error':'Platform not found'},status=status.HTTP_404_NOT_FOUND)
            
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except:
            return Response({'error':'Platform not found'},status=status.HTTP_404_NOT_FOUND)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# class ReviewDetail(mixins.RetrieveModelMixin,
#                    generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)







# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)



# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request, pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#     except:
#         return Response({'error':'movie not found'},status=status.HTTP_404_NOT_FOUND)
        
    
    
#     if request.method == 'GET':
#         #movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         #movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
#     if request.method == 'DELETE':
#         #movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


