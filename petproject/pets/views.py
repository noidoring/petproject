from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string

def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'pets/index.html', data)


def about(request):
    return render(request, 'pets/about.html')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'{cat_slug}')

def categories(request, cat_id):
    return HttpResponse(f'{cat_id}')

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def addpost(request):
    return HttpResponse('Страница добавления поста')


def contact(request):
    return HttpResponse('Страница для контакта')


def some_func(request):
    return HttpResponse('dfdf')
