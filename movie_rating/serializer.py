from django.db.models import fields
from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):          # serializer is used for converting complex datatype into native python datatype
    
   class Meta:
       model=Movie
       fields='__all__'
        