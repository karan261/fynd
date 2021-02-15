from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import status,viewsets
from django.http import Http404

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

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
    
    
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['name','director','genre']
    ordering_fields=['name','popularity','imdb_score']
    def get_queryset(self):
        global queryset,f
        order_query= self.request.query_params.get('ordering',None)
        search_query= self.request.query_params.get('search',None)
        print('search_query---->>>',search_query)
        if search_query:
            search_query = TextBlob(search_query)
            queryset = Movie.objects.filter(name__icontains=search_query.correct())
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


