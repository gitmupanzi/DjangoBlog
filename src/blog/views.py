from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from blog.models import BlogPost, Book

# Create your views here.
def blog_post(request):
    articles = BlogPost.objects.all()  # Récupère tous les articles
    return render(request, "blog/index_post.html", context={'posts': articles})

def blog_posts(request, slug):
    articles_slug = get_object_or_404(BlogPost, slug=slug)  # Utilise le slug pour récupérer l'article
    return render(request, 'blog/post.html', {'posts': articles_slug})

def books(request):
    books_titles=Book.objects.all()
    return render(request, "blog/index_book.html", context={'livres': books_titles})

def book(request, book_pk):
    book=get_object_or_404(Book, pk=book_pk)
    return render(request, "blog/book.html", context={'livres': book})



