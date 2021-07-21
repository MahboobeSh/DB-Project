from movie.views import movie_list
from django.contrib import admin
from .models import User, ProUser, Movie, SpecialMovie, Watch, Opinion, SpecialMovieWatch, Tag, List, MovieTag
# Register your models here.

admin.site.register(User)
admin.site.register(ProUser)
admin.site.register(Movie)
admin.site.register(SpecialMovie)
admin.site.register(Watch)
admin.site.register(Opinion)
admin.site.register(SpecialMovieWatch)
admin.site.register(Tag)
admin.site.register(List)
admin.site.register(MovieTag)