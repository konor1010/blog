from django.shortcuts import render, get_object_or_404
from news.models import News, Comments
from news.forms import CommentForm
from django.views import View
from django.http import HttpResponse
# Create your views here.

def news_list(request):
    """"Вывод всех ноавостей"""
    news = News.objects.all()
    return render(request, "news/news_list.html", {"news":news})

def new_single(reuest, pk):
    """Вывод полной статьи"""
    new = get_object_or_404(News, id = pk)
    comment = Comments.objects.filter(new=pk)
    form = CommentForm()
    return render(reuest, "news/new_single.html", {"new": new, "comments": comment, 'form': form})



