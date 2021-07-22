from django.db import models
from django.db.models.base import Model

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=11)
    password = models.CharField(max_length=20)
    nationalID = models.CharField(max_length=10, null=True)
    wallet = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    introducer = models.ForeignKey('self',null=True, blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.username


class ProUser(models.Model):
    prouser = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    expr_date = models.DateField()


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    year = models.IntegerField()
    description = models.CharField(max_length=1024)
    producer = models.CharField(max_length=1024)
    file = models.CharField(max_length=256)
    def __str__(self):
        return self.title

class SpecialMovie(models.Model):
    special_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, primary_key=True)
    price = models.IntegerField()


class Watch(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watch_time = models.DateTimeField(auto_now_add=True)



class SpecialMovieWatch(models.Model):
    movie = models.ForeignKey(SpecialMovie, on_delete=models.CASCADE)
    user = models.ForeignKey(ProUser, on_delete=models.CASCADE)
    watch_time = models.DateTimeField(auto_now_add=True)


class Opinion(models.Model):
    rate = models.IntegerField()
    comment = models.CharField(max_length=256, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class MovieTag(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)



class List(models.Model):
    list_id = models.AutoField(primary_key=True)
    prouser= models.ForeignKey(ProUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=1024)


class MovieList(models.Model):
    movie_list_id = models.AutoField(primary_key=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    moive = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['list_id', 'movie_id'], name='test')
        ]



