from django.urls import path
from . import views
urlpatterns = [
    path('landing', views.index),
    path('books', views.books),
    path('authors', views.authors),
    path('addbook', views.addbook),
    path('addauthor', views.addauthor),
    path('books/<nom>', views.deploybook),
    path('authors/<nam>',views.deployauthor),
]
