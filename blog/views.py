from django.shortcuts import render
from blog.models import Article
# ページャー
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    posts = Article.objects.all()
    # ページャーを有効化
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    data = {
        'posts': posts,
        'page_obj':paginator.get_page(page_number)
    }
    return render(request, 'blog/archive_article.html', data)

# 記事詳細
def article(request, pk):
    post = Article.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/article.html', context)