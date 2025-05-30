from datetime import date
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from posts.models import BlogPost

# Create your views here.

class BlogHome(ListView):
    model=BlogPost
    context_object_name = 'posts'
    template_name = 'posts/blogpost_list.html'

    
    def get_queryset(self):
        queryset= super().get_queryset()
        #  Vérifier si l'utilisateur est authentifié et filtrer les articles en conséquence
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True) 
      

class BlogPostDetail(DetailView): # R : Read
    model=BlogPost
    context_object_name = 'post'
    template_name = 'posts/blogpost_detail.html'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['post']=self.object
        return context

class BlogPostCreate(CreateView): # C : Create
    model= BlogPost
    template_name="posts/create_post.html"
    fields=['title','content','published','thumbnail',]
    success_url=reverse_lazy("posts:home") 
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author=self.request.user
            form.instance.published=True  # Définit la publication par défaut à False
            if form.instance.created_on is None:
                form.instance.created_on=date.today()  # Définit la date de création à aujourd'hui
        else:
            form.instance.author=None  # Définit l'auteur à None si l'utilisateur n'est pas connecté
            form.instance.published=True  # Définit la publication par défaut à True
            if form.instance.created_on is None:
                form.instance.created_on=date.today()  # Définit la date de création à aujourd'hui
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['submit_text']="Créer"
        return context 

class BlogPostUpdate(UpdateView): # U : Update
    model= BlogPost
    template_name="posts/create_post.html"
    fields=['title','content','published','thumbnail',]
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['submit_text']="Modifier"
        return context

@method_decorator(login_required, name='dispatch')
class BlogPostDelete(DeleteView): # D : Delete
    model=BlogPost
    template_name='posts/delete_post.html'
    context_object_name='post'
    success_url=reverse_lazy("posts:home")  # Redirige vers la liste des articles après la suppression
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['submit_text']="Oui, Supprimer"
        return context

    
