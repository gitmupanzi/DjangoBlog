import os
import django

# Configurez les paramètres Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")  # Remplacez "website.settings" par le chemin vers vos paramètres Django
django.setup()

import json
from blog.models import BlogPost

chemin = "D:\\Projet\\website\\src\\blog_blogpost.json"

with open(chemin, "r") as f:
    data = json.load(f)
    
for bp in data:
    BlogPost.objects.create(
        title=bp["title"],
        slug=bp["slug"],
        published=bp["published"],
        description=bp["description"],
        date=bp["date"]
    )