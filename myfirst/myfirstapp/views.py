from django.http import HttpResponse
from django.http import HttpResponseNotFound, Http404

from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse('Страница приложения MyfirstApp')


def categories(request, catid):
    if request.GET:
        print(request.GET)

    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}<p>')


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True
                        )
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')


def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")

