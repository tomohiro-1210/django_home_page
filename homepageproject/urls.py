from django.contrib import admin
from django.urls import path, include
from myhomepage import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('blog/', include('blog.urls')),
    path('login', views.Login.as_view()),
    # ログアウト、動作しない
    path('logout/', LogoutView.as_view(), name='logout'),
    # アカウント登録
    path('signup/', views.signup),
]
