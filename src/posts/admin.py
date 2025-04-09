from django.contrib import admin
from posts.models import BlogPost

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', "last_updated",'published','slug')
    list_editable = ('published',)

admin.site.register(BlogPost, BlogPostAdmin)