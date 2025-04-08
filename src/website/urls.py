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


from django.contrib import admin
from django.urls import path
from django.views import View
from blog.views import homeView, BlogIndexView,BlogPostDetailView, BlogPostCreateView,BlogPostUpdateView,BlogPostDeleteView,books, book, signup,bookform,creation_livre

urlpatterns = [
    path('', homeView.as_view(), name='home'),  # Vue pour la page d'accueil
    path('home/', homeView.as_view(), name='home'),  # Vue pour la page d'accueil
    path('admin/', admin.site.urls),
    # CRUD pour le model BlogPost
    path('blog/',  BlogIndexView.as_view(), name='blog_index'),  
    path('blog/create/', BlogPostCreateView.as_view(), name='blog_create'), 
    path('blog/<str:slug>/', BlogPostDetailView.as_view(), name='blog_post'),
    path('blog/<str:slug>/edit/', BlogPostUpdateView.as_view(), name='blog_edit'),  
    path('blog/<str:slug>/delete/', BlogPostDeleteView.as_view(), name='blog_delete'),
    
    # CRUD pour le model Author
    path('signup/', signup, name='signup'),
    
    
    # CRUD pour le model Book
    path('books/', books, name='book_index'),  # Vue pour la liste des livres
    path('books/<int:book_pk>/', book, name='book_post'),  # Vue pour un livre spécifique
    path('booksForm/', creation_livre, name='bookForm_index'),
    path('booksForm/<int:book_pk>/', bookform, name='bookForm_post'),   
]
