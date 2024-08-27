from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Article
# ログインやログアウトのテンプレを読み込む
from django.contrib.auth.views import LoginView, LogoutView
from myhomepage.forms import *
from django.contrib import messages


# Create your views here.
def index(request):
    articles = Article.objects.all()[:2]
    context = {
        'articles': articles
    }
    return render(request, 'mysite/index.html', context)

# ログイン
def login(request):
    data = {}
    if request.method == 'POST':
        data['req'] = request.POST
    return render(request, 'mysite/auth.html', data)

class Login(LoginView):
    template_name = 'mysite/auth.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'ログイン完了！！')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'エラーあり！！！')
        return super().form_invalid(form)
    
    
# 登録
def signup(request):
    data = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user.is_active = False
            user.save()
            messages.success(request, '登録完了！！')
            return redirect('/')
    return render(request, 'mysite/auth.html', data)