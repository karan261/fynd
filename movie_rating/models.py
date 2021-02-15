from django.db import models

# here we used to create the database or model 
class Movie(models.Model):
    id=models.AutoField(primary_key=True)
    popularity = models.FloatField(max_length=10)
    director = models.CharField(max_length=25)
    genre=models.JSONField(max_length=10)
    imdb_score=models.FloatField(max_length=3)
    name=models.CharField(max_length=100)

 