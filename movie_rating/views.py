from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import status,viewsets
from django.http import Http404
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Movie
from .serializer import MovieSerializer
from textblob import TextBlob


# Create your views here.

global queryset      
f=0


class MovieViewSet(viewsets.ViewSet,ListAPIView):
    global queryset
    queryset=Movie.objects.all()                       # queryset is used for reterving a collections of objects from your database
    serializer_class=MovieSerializer                   # serializer is used for converting complex datatype into native python datatype 
    filter_backends=[SearchFilter,OrderingFilter]      # SearchFilter is used for searching purpose by filter the particular item by its key name provided in search_fields()
    search_fields=['name','director','genre']          # OrderingFilter is used for sorting a particular item or collection
    ordering_fields=['name','popularity','imdb_score']

    def get_queryset(self):                             # get_queryset() method is used for determines the list of objects that you want to display
        global queryset,f
        order_query= self.request.query_params.get('ordering',None)
        search_query= self.request.query_params.get('search',None)

        if search_query:
            search_query = TextBlob(search_query)       # TextBlob() is module used for spell checker or auto correction
            queryset = Movie.objects.filter(name__icontains=search_query.correct())
            if not queryset:
                f=1
                    
        elif order_query:
            queryset = Movie.objects.all().order_by(order_query)
            
           
        else:
            f=0
            queryset=Movie.objects.none()
        return queryset
    
    
   
    def list(self,request):                             # list() method is used for reterving all objects from your database
        global queryset,f
       
        if f==1:
            f=0
            queryset=Movie.objects.none()
            serializer=MovieSerializer(queryset,many=True)
            return Response({"msg":"Sorry Movie is not avilable"})
        
        elif queryset:
            serializer=MovieSerializer(queryset,many=True)
            return Response(serializer.data)
            
        else:
            mv=Movie.objects.all()
            serializer=MovieSerializer(mv,many=True)
            return Response(serializer.data)
            
    def retrieve(self,request,pk=None):                 # retrieve() method act as a get() function  used for fetch a particular object from your database
        id=pk
        if id is not None:
            # mv=Movie.objects.get(id=id)
            try:
                mv=Movie.objects.get(id=id)
            except Movie.DoesNotExist:
                raise Http404
            serializer=MovieSerializer(mv)
            return Response(serializer.data)
        
    def create(self,request):                           # create() method act as a post() function used for creating a new object in your database
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'New Movie Details Added'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):                        # update() method act as a put() function used for updating a particular object in your database
        id=pk
        mv=Movie.objects.get(pk=id)
        serializer=MovieSerializer(mv,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Movie Details Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):               # partial_update() method act as a patch() function used for partial updating a particular object in your database
        id=pk
        mv=Movie.objects.get(pk=id)
        serializer=MovieSerializer(mv,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Movie Details Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):                      # destroy() method act as delete() function used for deleting a particular object from your database
        id=pk
        mv=Movie.objects.get(pk=id)
        mv.delete()
        return Response({'msg':'Movie Details Deleted'})


