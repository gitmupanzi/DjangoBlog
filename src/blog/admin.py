from django.contrib import admin

# Register your models here.
from blog.models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','published', 'date', 'author')
    empty_value_display = '-'
    list_editable = ('published', 'date')
    search_fields = ('title', 'content')
    list_filter = ('author', 'published')
    autocomplete_fields = ('author',) # Autocomplete pour le champ author
    list_per_page = 10 # Nombre d'articles par page dans l'admin



