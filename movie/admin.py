from django.contrib import admin
from .models import User, ProUser, Movie, SepecialMovie, Watch, Opinion, SepecialMovieWatch, Tag
# Register your models here.

admin.site.register(User)
admin.site.register(ProUser)
admin.site.register(Movie)
admin.site.register(SepecialMovie)
admin.site.register(Watch)
admin.site.register(Opinion)
admin.site.register(SepecialMovieWatch)
admin.site.register(Tag)