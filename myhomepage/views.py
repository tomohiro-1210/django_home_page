from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Article


# Create your views here.
def index(request):
    articles = Article.objects.all()[:2]
    context = {
        'articles': articles
    }
    return render(request, 'mysite/index.html', context)