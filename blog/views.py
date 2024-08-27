from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.
def blogtop(request):
    return HttpResponse('ブログTOPページは特に何もありません。')

# 記事詳細
def article(request, pk):
    post = Article.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/article.html', context)