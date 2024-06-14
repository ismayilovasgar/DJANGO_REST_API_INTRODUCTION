from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="Blog Images", blank=True, null=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class MovieModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=300)
    director = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    release_year = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.director}"

    class Meta:
        db_table = "MovieModel"
