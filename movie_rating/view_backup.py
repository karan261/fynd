from re import search

from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (authentication,  serializers, status,
                            viewsets)
from rest_framework.authentication import SessionAuthentication

from rest_framework.generics import ListAPIView
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response



from .models import Movie
from .serializer import MovieSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.settings import api_settings
from django.http import Http404
from django.db.models import Q
# Create your views here.



# class MovieList(ListAPIView):
#     queryset = Movie.objects.all()
#     serializer_class=MovieSerializer
#     filter_backends=[OrderingFilter]
#     # filter_backends=[SearchFilter]
#     # search_fields=['name']
#     def get_queryset(self):
#         name = self.request.query_params.get('ordering',None)
#         # print('---->>>',name)
#         if name:
#             queryset = Movie.objects.all().order_by(name)
#             print('---->>>',queryset)
#         queryset=Movie.objects.all()
#         return queryset
    
   
    
# print('queryset----->',queryset)

    # search_fields=['name','imdb_score']
    # print(queryset)
    # serializer_class = MovieSerializer
    # filter_backends=[DjangoFilterBackend]
    # filterset_fields=['name']
    # pass
    # queryset = Movie.objects.all()
    # serializer_class = MovieSerializer
    # filterset_fields=['name']
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['username', 'email']

global queryset
f=0


class MovieViewSet(viewsets.ViewSet,ListAPIView):
    global queryset
    
    
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['name','director','genre']
    def get_queryset(self):
        global queryset,f
        order_query= self.request.query_params.get('ordering',None)
        search_query= self.request.query_params.get('search',None)
        print('search_query---->>>',search_query)
        if search_query:
            queryset = Movie.objects.filter(Q(name__icontains=search_query)|Q(director__icontains=search_query)|Q(genre__in=['family']))
            print('\n 1-->>>>>',queryset)
            if not queryset:
                f=1
                
                
                

            
        elif order_query:
            queryset = Movie.objects.all().order_by(order_query)
            print('\n 2-->>>>>',queryset)
           
        else:
            f=0
            queryset=Movie.objects.none()
            print('\n 3-->>>>>',queryset)
        return queryset
    
    
   
    def list(self,request):
        print("\nhelllo\n")
        global queryset,f
        print('f-----',f)
        # print('----->',queryset)
        # queryset = Movie.objects.all()
        if f==1:
            f=0
            queryset=Movie.objects.none()
            serializer=MovieSerializer(queryset,many=True)
            print('\n 1----->',f)
            return Response({"msg":"Sorry Movie is not avilable"})
        
        elif queryset:
            print('\n 4-->>>>>',queryset)
            serializer=MovieSerializer(queryset,many=True)
            print("dashad")
            return Response(serializer.data)
            
        else:
            print('\n 5-->>>>>',queryset)
            mv=Movie.objects.all()
            serializer=MovieSerializer(mv,many=True)
            print("asda")
            return Response(serializer.data)
            
        
        
        
        # return Response(serializer.data)
        

        
        # mv=Movie.objects.all()
        # serializer=MovieSerializer(mv,many=True)
        
        
        
    
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            # mv=Movie.objects.get(id=id)
            try:
                mv=Movie.objects.get(id=id)
            except Movie.DoesNotExist:
                raise Http404
            serializer=MovieSerializer(mv)
            return Response(serializer.data)
        
        

    def create(self,request):
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'New Movie Details Added'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        id=pk
        mv=Movie.objects.get(pk=id)
        serializer=MovieSerializer(mv,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Movie Details Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id=pk
        mv=Movie.objects.get(pk=id)
        serializer=MovieSerializer(mv,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Movie Details Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        id=pk
        mv=Movie.objects.get(pk=id)
        mv.delete()
        return Response({'msg':'Movie Details Deleted'})


# class MovieApi(APIView):
#     queryset = Movie.objects.all()
#     serializer_class=MovieSerializer
#     filter_backends=[SearchFilter]
#     search_fields=['name']


#     def get(self,request,pk=None,format=None):
#         id=pk
#         if id is not None:
#             mv=Movie.objects.get(id=id)
#             serializer=MovieSerializer(mv)
#             return Response(serializer.data)
        
#         mv=Movie.objects.all()
#         serializer=MovieSerializer(mv,many=True)
#         return Response(serializer.data)
    


#     def create(self,request):
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'New Movie Details Added'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.status.HTTP_400_BAD_REQUEST)
    
#     def put(self,request,pk):
#         id=pk
#         mv=Movie.objects.get(pk=id)
#         serializer=MovieSerializer(mv,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Movie Details Updated'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.status.HTTP_400_BAD_REQUEST)
    
#     def patch(self,request,pk):
#         id=pk
#         mv=Movie.objects.get(pk=id)
#         serializer=MovieSerializer(mv,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Movie Details Updated'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         id=pk
#         mv=Movie.objects.get(pk=id)
#         mv.delete()
#         return Response({'msg':'Movie Details Deleted'})
