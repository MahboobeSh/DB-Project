from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile/<int:user_id>/addintroducer/', views.addIntroducer, name='addIntroducer'),
    path('profile/<int:user_id>/raisewallet/', views.raiseWallet, name='raiseWallet'),
    path('profile/<int:user_id>/createlist/', views.createList, name='createlist'),
    path('addpro/', views.add_pro, name='addpro'),
    path('list/<int:list_id>/', views.list_detail, name='list_detail'),
    path('list/<int:list_id>/addtolist/', views.addToList, name='addtolist'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/search/', views.movie_search, name='movie_search'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movie/<int:movie_id>/addcomment/', views.addComment, name='comment'),
    path('movie/<int:movie_id>/watch/', views.watch_movie, name='watch_moive'),
    # ex: /polls/5/results/
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    # ex: /polls/5/vote/
    
    
]