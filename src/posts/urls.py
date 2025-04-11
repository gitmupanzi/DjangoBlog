from django.urls import path
from posts.views import BlogHome, BlogPostCreate, BlogPostDelete, BlogPostDetail, BlogPostUpdate


app_name = 'posts'  # Nom de l'application pour les URL inversées
urlpatterns = [
    path('', BlogHome.as_view(), name='home'), 
    path('create/', BlogPostCreate.as_view(), name='create'),
    path('<str:slug>/', BlogPostDetail.as_view(), name='detail'), 
    path('edit/<str:slug>/', BlogPostUpdate.as_view(), name='edit'),  
    path('delete/<str:slug>/', BlogPostDelete.as_view(), name='delete'),
    path('delete/<int:pk>/', BlogPostDelete.as_view(), name='delete'),  # Utiliser pk si nécessaire   
]
