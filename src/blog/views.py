from datetime import date
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from blog.models import BlogPost, Book
from website.forms import BlogPostForm, SignupForm,BookForm
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView


# Views basé sur des classes. CRUD
# C : Create, R : Retrieve, U : Update, D : Delete
## Class BlogPost
class BlogIndex(ListView): # R : Retrieve multiple : on affiche tous les articles
    model=BlogPost
    template_name="blog/index_post.html"
    context_object_name="posts"  # Nom de la variable dans le template
   # queryset=BlogPost.objects.filter(published=False)  # Filtre les articles publiés

    def get_queryset(self):
        queryset= super().get_queryset()
        #  Vérifier si l'utilisateur est authentifié et filtrer les articles en conséquence
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True) 

@method_decorator(login_required, name='dispatch')
class BlogPostDetail(DetailView): # R : Retrieve individuel : on affiche un article
    model=BlogPost
    template_name="blog/post.html"
    context_object_name="post"  # Nom de la variable dans le template

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['post']=self.object
        return context
@method_decorator(login_required, name='dispatch')
class BlogPostCreate(CreateView): # C : Create
    model= BlogPost
    template_name="blog/create_post.html"
    form_class=BlogPostForm # Utilise le formulaire défini dans forms.py
    success_url=reverse_lazy("blog:blog_index")  # URL de redirection après la création réussie de l'article
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author=self.request.user
        
        form.instance.published=True  # Définit la publication par défaut à False
        form.instance.date=date.today()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['submit_text']="Créer"
        return context
@method_decorator(login_required, name='dispatch')
class BlogPostUpdate(UpdateView): # U : Update
    model=BlogPost
    template_name="blog/create_post.html"
    context_object_name="post"
    form_class=BlogPostForm # Utilise le formulaire défini dans forms.py
    access_url=reverse_lazy('blog:blog_index')  # URL de redirection après la mise à jour réussie de l'article
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['submit_text']="Modifier"
        return context
@method_decorator(login_required, name='dispatch')
class BlogPostDelete(DeleteView): # D : Delete
    model=BlogPost
    template_name="blog/delete_post.html"
    context_object_name="post"  # Nom de la variable dans le template
    success_url=reverse_lazy("blog:blog_index")  # URL de redirection après la création réussie de l'article
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['submit_text']="Supprimer"
        return context
    
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

