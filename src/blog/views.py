from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from blog.models import BlogPost, Book
from website.forms import BlogPostForm, SignupForm,BookForm
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView,DetailView


# Views basé sur des classes. CRUD

## Class
class homeView(TemplateView):
    template_name="blog/home.html"
    title="blog home"
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']=self.title
        return context

    def __str__(self):
        return super().title

## Class BlogPost
class BlogPostCreateView(CreateView): # C : Create
    model= BlogPost
    template_name="blog/create_post.html"
    form_class=BlogPostForm # Utilise le formulaire défini dans forms.py
    success_url=reverse_lazy('blog_index')  # URL de redirection après la création réussie de l'article
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author=self.request.user
        
        form.instance.published=True  # Définit la publication par défaut à False
        form.instance.date=datetime.today()
        
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['submit_text']="Créer"
        return context
    
    
class BlogIndexView(ListView): # R : Retrieve multiple : on affiche tous les articles
    model=BlogPost
    template_name="blog/index_post.html"
    context_object_name="posts"  # Nom de la variable dans le template
   # queryset=BlogPost.objects.filter(published=False)  # Filtre les articles publiés
class BlogPostDetailView(DetailView): # R : Retrieve individuel : on affiche un article
    model=BlogPost
    template_name="blog/post.html"
    context_object_name="post"  # Nom de la variable dans le template


class BlogPostUpdateView(UpdateView): # U : Update
    model=BlogPost
    template_name="blog/create_post.html"
    form_class=BlogPostForm # Utilise le formulaire défini dans forms.py
    access_url=reverse_lazy('blog_index')  # URL de redirection après la création réussie de l'article
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['submit_text']="Modifier"
        return context
    
class BlogPostDeleteView(DeleteView): # D : Delete
    model=BlogPost
    template_name="blog/delete_post.html"
    context_object_name="post"  # Nom de la variable dans le template
    success_url=reverse_lazy('blog_index')  # URL de redirection après la création réussie de l'article
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['submit_text']="Supprimer"
        return context
    

## Class Author
    


# Views basé sur des fonctions.
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

