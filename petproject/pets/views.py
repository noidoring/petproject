from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

def index(request):
    return HttpResponse('main')


def categories(request, cat_id):
    return HttpResponse(f'Categories {cat_id}')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'{cat_slug}')


def archive(request, year):
    if year > 2023:
        return HttpResponseRedirect('/')
    
    return HttpResponse(f'{year}')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
