"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from turtle import home
from django.contrib import admin
from django.urls import path
from blog.views import blog_post,blog_posts, books, book, creation_article, signup,bookform,creation_livre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog_post, name='blog_index'),  # Vue pour la liste des blogs
    path('blog/<slug:slug>/', blog_posts, name='blog_post'),  # Vue pour un article spécifique
    path('books/', books, name='book_index'),  # Vue pour la liste des livres
    path('books/<int:book_pk>/', book, name='book_post'),  # Vue pour un livre spécifique
    path('signup/', signup, name='signup'),  # Vue pour le formulaire d'inscription
    path('article/', creation_article, name='blog_articles'),  
    path('booksForm/', creation_livre, name='bookForm_index'),
    path('booksForm/<int:book_pk>/', bookform, name='bookForm_post'),
    
 
    
]
