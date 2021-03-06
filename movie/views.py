from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, MovieLink


class MovieList(ListView):
    model = Movie
    paginate_by=1
    
    


class MovieDetail(DetailView):
    model = Movie
    

    def get_object(self):
        object = super(MovieDetail, self).get_object()
        object.views_count +=1
        object.save()
        return object
    

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['links'] = MovieLink.objects.filter(movie=self.get_object())
        return context

class MovieCategory(ListView):
    model = Movie
    paginate_by=1

    def get_queryset(self):
        self.category = self.kwargs['category']
        return Movie.objects.filter(category=self.category)

    
    def get_context_data(self, **kwargs):
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context['movie_category'] = self.category
        return context


class MovieLanguage(ListView):
    model = Movie
    paginate_by=1

    def get_queryset(self):
        self.language = self.kwargs['lang']
        return Movie.objects.filter(language=self.language)

    
    def get_context_data(self, **kwargs):
        context = super(MovieLanguage, self).get_context_data(**kwargs)
        context['movie_language'] = self.language
        return context