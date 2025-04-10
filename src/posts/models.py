from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
user = get_user_model() # l'utilisateur est défini dans le settings.py

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Title")
    slug= models.SlugField(max_length=255, unique=True, blank=True, verbose_name="Slug")
    author = models.ForeignKey(user, on_delete=models.SET_NULL,null=True,blank=True, verbose_name="Author",related_name="website_posts")
    last_updated= models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    created_on=models.DateField(blank=True, null=True, verbose_name="Created On")
    published=models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, null=True, verbose_name="Contenu")
    thumbnail=models.ImageField(blank=True, upload_to='posts')
    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
            
        super().save(*args, **kwargs)
    
    @property
    def author_or_default(self):
        if self.author:
            return self.author.username
        else:
            return "Auteur inconnu"
    def get_absolute_url(self):
        return reverse('posts:home')
