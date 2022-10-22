from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):  # HttpRequest
    return HttpResponse("Страница приложения women.")


def categories(request, catid):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2020:
        # raise Http404()
        return redirect('home', permanent=True)  # постоянный редирект
        # return redirect('/')

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def test(request):
    return HttpResponse("<h2>Это тестовая страница</h2>")


