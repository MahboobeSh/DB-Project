from django.db import models
from django.db.models.base import Model

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=11)
    password = models.CharField(max_length=20)
    nationalID = models.CharField(max_length=10)
    wallet = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    introducer = models.ForeignKey('self',null=True, blank=True,on_delete=models.SET_NULL)


class ProUser(models.Model):
    prouser_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    expr_date = models.DateField()


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    year = models.IntegerField()
    description = models.CharField(max_length=1024)
    producer = models.CharField(max_length=1024)
    file = models.CharField(max_length=256)

class SepecialMovie(models.Model):
    special_movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, primary_key=True)
    price = models.IntegerField()


class Watch(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    watch_time = models.DateTimeField(auto_now_add=True)



class SepecialMovieWatch(models.Model):
    movie_id = models.ForeignKey(SepecialMovie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    watch_time = models.DateTimeField(auto_now_add=True)


class Opinion(models.Model):
    rate = models.IntegerField()
    comment = models.CharField(max_length=256, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)

class MovieTag(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)



class List(models.Model):
    list_id = models.AutoField(primary_key=True)
    prouser_id = models.ForeignKey(ProUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)

class MovieList(models.Model):
    list_id = models.AutoField(primary_key=True)
    models.ForeignKey(Movie, on_delete=models.CASCADE)

