from django.urls import path
from blog.views import BlogIndex,BlogPostCreate, BlogPostDelete, BlogPostDetail, BlogPostUpdate, signup, books, book, creation_livre, bookform

app_name = 'blog'  # Nom de l'application pour les URL inversées
urlpatterns = [
        path('',  BlogIndex.as_view(), name='blog_index'), 
        path('create/', BlogPostCreate.as_view(), name='blog_create'),
        path('<str:slug>/', BlogPostDetail.as_view(), name='blog_post'),
        path('edit/<str:slug>/', BlogPostUpdate.as_view(), name='blog_edit'),  
        path('delete/<str:slug>/', BlogPostDelete.as_view(), name='blog_delete'),
        path('signup/', signup, name='signup'), # type: ignore
        path('books/', books, name='book_index'),  # Vue pour la liste des livres
        path('books/<int:book_pk>/', book, name='book_post'),  # Vue pour un livre spécifique
        path('booksForm/', creation_livre, name='bookForm_index'),
        path('booksForm/<int:book_pk>/', bookform, name='bookForm_post'),
            
]