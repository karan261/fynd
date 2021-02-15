

from django.test import TestCase
from django.urls import reverse
from .models import Movie


# Create your tests here.
class MovieTest(TestCase):
    
    # Testcase for creation of model Movie 
    def test_model_create(self):
        movie=Movie.objects.create(
            popularity=88.0,
            director="yash raj",
            genre=["romantic","musical","drama"],
            imdb_score=9.0,
            name="ddlj"
        )
        movie_result=Movie.objects.last()
        self.assertEqual(movie.name,"ddlj")
        self.assertEqual(movie.imdb_score,9.0)

    # Testcase for fetching  a particular movie object from the API
    def test_get_url(self):
        response=self.client.get(reverse("movie-detail",kwargs={"pk": 85}))
        self.assertEqual(response.status_code,200)
        
    # Testcase for posting a new movie object to the API
    def test_post_url(self):
        input_data={
            "popularity" : 99.0,
            "director":"Rohit Shetty",
            "genre":["romantic","musical","drama"],
            "imdb_score":9.2,
            "name":"dilwale"
        }

        url=reverse('movie-list')
        response=self.client.post(url,data=input_data)
        self.assertEqual(response.status_code,201)

    # Testcase for deleting a particular  Movie object from the API 
    def test_delete_url(self):
        response=self.client.delete(reverse("movie-detail",kwargs={"pk": 85}))
        self.assertEqual(response.status_code,204)

    

    


    