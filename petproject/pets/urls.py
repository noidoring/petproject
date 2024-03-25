from django.urls import path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'), 
    path('about/', views.about),
    path('cats/<int:cat_id>/', views.categories),
    path('cats/<slug:cat_slug>', views.categories_by_slug),
    path('archive/<year4:year>/', views.archive),
    path('addpost/', views.addpost),
]