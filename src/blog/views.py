from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from blog.models import BlogPost, Book
from website.forms import BlogPostForm, SignupForm,BookForm
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def signup(request):
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form=SignupForm(request.GET)
    
    return render(request, "blog/signup.html", context={'form': form})


def creation_article(request): # utilise le formulaire (forms.py) : BlogPostForm
    if request.method=="POST":
        form=BlogPostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return HttpResponseRedirect(request.path)
    else:
        init_values={}
        if request.user.is_authenticated:
            init_values["author"]=request.user
            init_values["date"]=datetime.today
        form=BlogPostForm(initial=init_values)
    return render (request, "blog/article.html", context={"form":form})

def bookform(request, book_pk):
    book=get_object_or_404(Book, pk=book_pk)
    return render(request, "blog/bookForm.html", context={'livres': book})

@csrf_exempt
def creation_livre(request):  
    if request.method=="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return HttpResponseRedirect(request.path)
    else:
        init_values={}
        if request.user.is_authenticated:
            init_values["author"]=request.user
        form=BookForm(initial=init_values)
    livres = Book.objects.all()  # Liste des livres depuis la BDD
    return render(request, "blog/index_bookForm.html", {"livres": livres, "livresForm": form})  

