from django.shortcuts import render
from .models import Movie
from django.core.paginator import Paginator
# Create your views here.

def movie_list(request):
    movie_object = Movie.objects.all()

    #Search
    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        movie_object = movie_object.filter(name__icontains=movie_name)

    #Pagination
    paginator = Paginator(movie_object,3)
    page = request.GET.get('page')
    movie_object = paginator.get_page(page)
    
    return render(request,'mainapp/index.html',{"movie_object":movie_object})
