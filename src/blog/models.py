from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=36)
    slug=models.SlugField()

    
class BlogPost(models.Model):
    author=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category=models.ManyToManyField(Category)
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    published=models.BooleanField(default=False)
    date=models.DateField(blank=True, null=True)
    content=models.TextField()
    description=models.TextField(blank=True)
    
    class Meta:
        verbose_name="Article"
        verbose_name_plural="Articles"
        ordering=["title"]
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_post", kwargs={"slug": self.slug})
    
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)
    
   
    def number_of_words(self):
        return len(self.content.split())
    

class Author(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    wikipedia=models.URLField()
        
    class Meta:
        verbose_name="Auteur"
        verbose_name_plural="Auteurs"
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Book(models.Model):
    title=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    summary=models.TextField(blank=True)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    category_choices = [
        ("Aventure", "Aventure"),
        ("Thriller", "Thriller"),
        ("Fantastique", "Fantastique"),
        ("Romance", "Romance"),
        ("Horreur", "Horreur"),
        ("Science-fiction", "Science-fiction"),
        ("Science", "Science"),
    ]
    category = models.CharField(max_length=20, choices=category_choices)
    stock=models.IntegerField(default=0,blank=True)
    
    
    class Meta:
        verbose_name="Livre"
        verbose_name_plural="Livres"
        
    def __str__(self):
        return self.title




