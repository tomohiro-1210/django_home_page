from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blogtop(request):
    return HttpResponse('ブログTOPページは特に何もありません。')

def test(request):
    return HttpResponse('ブログURLテスト')