
from django.core import exceptions
from django.db.models.query_utils import Q
from django.http.response import HttpResponseBase
from django.shortcuts import render, get_object_or_404,redirect
from django.http import Http404

# Create your views here.
from django.http import HttpResponse
from .models import User,Movie,MovieTag,ProUser,SpecialMovie,Watch,SpecialMovieWatch,List,Opinion
from .forms import CommentForm, WatchForm, UserForm, LogInForm, IntroducerForm, WalletForm

def home(request):
    return render(request, "home.html")


def movie_detail(request, movie_id):
    try: 
        movie_obj = Movie.objects.get(movie_id= movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    form = CommentForm()
    context = {
        'movie': movie_obj,
        'commentForm':form,
    }
    return render(request, 'movie_detail.html', context)
    



def movie_list(request):
    movies_obj = Movie.objects.order_by('movie_id')[:5]
    context = {
        'movies_list': movies_obj,
        'title':"movies homepage"
    }
    return render(request, 'movies.html', context)

def movie_search(request):
    if request.method == 'GET':

        name = request.GET.get("name")
        tag = request.GET.get("tag")
        #year = request.GET.get("year")
        

        if name != None : 
            movies_obj = Movie.objects.filter(Q(producer__icontains=name))
        elif name == None:
            name=""
            movies_obj = Movie.objects.filter(Q(producer__icontains=name))

        context = {
            'movies_list': movies_obj,
            'title':"search result",
        }
        return render(request, 'movies.html', context)





def user_detail(request, user_id):
    return render(request, "home.html")


def watch_movie(request, movie_id):
    
    if request.method == "POST":
        try:
            user_id =request.session['user_id']
        except:
            return HttpResponse("you must login first")
        
        form = WatchForm(request.POST)

        obj = Watch()
        obj.user_id = user_id
        obj.movie_id = movie_id
        try:
            obj.save()
            return HttpResponse("you watched this movie")
        except:
            try:
                obj = SpecialMovieWatch()
                obj.user_id = user_id
                obj.movie_id = movie_id
                return HttpResponse("you watched this movie")
            except:
                return HttpResponse("you can not watch this movie")

    else:
        return HttpResponse("your request is not allowed")


    



def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_user = User()
            new_user.first_name = form.cleaned_data['firstname']
            new_user.last_name = form.cleaned_data['lastname']
            new_user.password = form.cleaned_data['password']
            new_user.email = form.cleaned_data['email']
            new_user.nationalID = form.cleaned_data['nationalID']
            new_user.phone_number = form.cleaned_data['phonenumber']
            new_user.username = form.cleaned_data['username']
            # redirect to a new URL:
            try:
                new_user.save()
                form = LogInForm
                return  render(request, 'login', {'form': form,'msg':"your account is created"} )  
            except:
                return render(request, 'register.html', {'form': form, 'error':'your account is not created database'}) 
        else: 
            return render(request, 'register.html', {'form': form, 'error':'your account is not created form is not valid'})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()


    return render(request, 'register.html', {'form': form})        



def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LogInForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            user_obj = get_object_or_404(User, username=username)
            # redirect to a new URL:
            if password == user_obj.password:
                request.session['user_id'] = user_obj.user_id
                
                return   render(request, 'home.html',{"msg":"you have logged in"})
            else:
                return render(request, 'login.html', {'form': form, 'error':'your password is not correct'}) 
        else: 
            return render(request, 'register.html', {'form': form, 'error':'your account is not created form is not valid'})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LogInForm()


    return render(request, 'login.html', {'form': form})   



def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")



def profile(request, user_id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            try:
                session_user_id =request.session['user_id']
            except:
                return HttpResponse("you must login first")
            
            if session_user_id != user_id:
                return HttpResponse("you cannot change another person information")

            try:
                new_user = User.objects.get(pk=user_id)
            except:
                return HttpResponse("this user is not availabe")
 

            new_user.first_name = form.cleaned_data['firstname']
            new_user.last_name = form.cleaned_data['lastname']
            new_user.password = form.cleaned_data['password']
            new_user.email = form.cleaned_data['email']
            new_user.nationalID = form.cleaned_data['nationalID']
            new_user.phone_number = form.cleaned_data['phonenumber']
            new_user.username = form.cleaned_data['username']
            # redirect to a new URL:
            try:
                new_user.save()
                return HttpResponse("your account is updated")
            except:
                user_obj = User.objects.get(pk=user_id)
                temp ={'firstname':user_obj.first_name,
                'lastname':user_obj.last_name,
                'username':user_obj.last_name,
                'email':user_obj.email,
                'nationalID': user_obj.nationalID,
                'phonenumber':user_obj.phone_number
                }
                form = UserForm(initial=temp)
                return render(request, 'profile.html', {'form': form, 'error':'your account is not updated on database'}) 
        else: 
            return render(request, 'register.html', {'form': form, 'error':'your account is not created form is not valid'})
    # if a GET (or any other method) we'll create a blank form
    else:
        try: 
            user_obj = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404("user does not exist")
        temp ={'firstname':user_obj.first_name,
                'lastname':user_obj.last_name,
                'username':user_obj.last_name,
                'email':user_obj.email,
                'nationalID': user_obj.nationalID,
                'phonenumber':user_obj.phone_number
        }
        form = UserForm(initial=temp)
        form2 = IntroducerForm()
        form3 = WalletForm()


    return render(request, 'profile.html', {'form': form, 'user':user_obj, 'form2': form2, 'form3':form3}) 



def addIntroducer(request,user_id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IntroducerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            try:
                session_user_id =request.session['user_id']
            except:
                return HttpResponse("you must login first")
            
            if session_user_id != user_id:
                return HttpResponse("you cannot change another person information")

            try:
                new_user = User.objects.get(pk=user_id)
            except:
                return HttpResponse("you must login first")
 

            introducer_username = form.cleaned_data['introducer_username']
            try: 
                introducer_obj = User.objects.get(username=introducer_username)
            except:
                return HttpResponse("introducer is not valid")

            new_user.introducer_id =  introducer_obj.user_id
            # redirect to a new URL:
            try:
                new_user.save()
                return HttpResponse("your introducer is added")
            except:
                return HttpResponse("your introducer is not added")
  
    # if a GET (or any other method) we'll create a blank form
    else:
        try: 
            user_obj = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404("user does not exist")
        temp ={'firstname':user_obj.first_name,
                'lastname':user_obj.last_name,
                'username':user_obj.last_name,
                'email':user_obj.email,
                'nationalID': user_obj.nationalID,
                'phonenumber':user_obj.phone_number
        }
        form = UserForm(initial=temp)
        form2 = IntroducerForm()
        form3 = WalletForm()


    return render(request, 'profile.html', {'form': form, 'user':user_obj, 'form2': form2, 'form3':form3}) 




def raiseWallet(request, user_id):
    if request.method == 'POST':
        
        form = WalletForm(request.POST)
        
        if form.is_valid():
            try:
                session_user_id =request.session['user_id']
            except:
                return render(request, 'login.html',{'msg': "you must login first to increase you wallet"})
            
            if session_user_id != user_id:
                return HttpResponse("you cannot change another person information")

            try:
                new_user = User.objects.get(pk=user_id)
            except:
                return HttpResponse("this user is not in our database")
 

            amount = form.cleaned_data['amount']
            


            new_user.wallet =  new_user.wallet + amount
            # redirect to a new URL:
            try:
                new_user.save()
                user_obj = new_user

                temp ={'firstname':user_obj.first_name,
                        'lastname':user_obj.last_name,
                        'username':user_obj.last_name,
                        'email':user_obj.email,
                        'nationalID': user_obj.nationalID,
                        'phonenumber':user_obj.phone_number
                }
                form = UserForm(initial=temp)
                form2 = IntroducerForm()
                form3 = WalletForm()
                return render(request, 'profile.html', {'form': form, 'user':new_user, 'form2': form2, 'form3':form3, 'msg':"your wallet increased"})
                
            except:
                return HttpResponse("you waallet could not increase")
        else:
            return HttpResponse("your form is not valid")
  
    # if a GET (or any other method) we'll create a blank form
    else:
        try: 
            user_obj = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404("user does not exist")

        temp ={'firstname':user_obj.first_name,
                'lastname':user_obj.last_name,
                'username':user_obj.last_name,
                'email':user_obj.email,
                'nationalID': user_obj.nationalID,
                'phonenumber':user_obj.phone_number
        }
        form = UserForm(initial=temp)
        form2 = IntroducerForm()
        form3 = WalletForm()

        return render(request, 'profile.html', {'form': form, 'user':user_obj, 'form2': form2, 'form3':form3})



def addComment(request, movie_id):
    if request.method == "POST":
        try:
            user_id =request.session['user_id']
        except:
            return HttpResponse("you must login first")
        
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = Opinion()
            obj.user_id = user_id
            obj.movie_id = movie_id
            obj.rate = form.cleaned_data['rate']
            obj.comment = form.cleaned_data['comment']
            try:
                obj.save()
                return HttpResponse("your comment is saved")
            except:

                    return HttpResponse("you can not add comment to  this movie")
        else:
            return HttpResponse("the form is not valid")

    else:
        return HttpResponse("your request is not allowed")



def createList(request):
    pass


def list_detail(request, list_id):
    pass


def addToList(request,list_id):
    pass

