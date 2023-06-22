from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime
# Create your views here.


class News(ListView):
    model = Post
    ordering = '-datetime_post_creation' #сортировка по дате создания
    # queryset = Post.objects.post_by('name')
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        # context['next_sale'] = "Распродажа в среду!"
        return context


class BreakingNews(DetailView):
    model = Post
    template_name = 'breaking_news.html'
    context_object_name = 'breaking_news'


class Articles(DetailView):
    model = Post
    template_name = 'articles.html'
    context_object_name = 'articles'

