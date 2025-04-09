from django import forms
from blog.models import BlogPost,Book

JOBS = [
    ('python', 'Développeur python'), 
    ('javascript', 'Développeur javascript'),
    ('csharp ', 'Développeur C#'),
    ('java', 'Développeur Java'), 
    ('php', 'Développeur PHP'), 
    ('html', 'Développeur HTML'), 
    ('css', 'Développeur CSS'), 
    ('swift', 'Développeur Swift'), 
    ('kotlin', 'Développeur Kotlin'), 
    ('ruby', 'Développeur Ruby'), 
    ('go', 'Développeur Go'), 
    ('typescript', 'Développeur TypeScript'),
    ('sql', 'Développeur SQL'), 
    ('rust', 'Développeur Rust'), 
    ('dart', 'Développeur Dart'), 
    ('html5', 'Développeur HTML5'), 
    ('css3', 'Développeur CSS3'), 
    ('xml', 'Développeur XML'), 
    ('json', 'Développeur JSON'), 
    ('yaml', 'Développeur YAML'), 
    ('markdown', 'Développeur Markdown'), 
    ('bash', 'Développeur Bash'), 
    ('powershell', 'Développeur PowerShell'), 
    ('typescriptreact', 'Développeur TypeScript React'),
]

class SignupForm(forms.Form):  
    pseudo=forms.CharField(label='Pseudo', max_length=100 ,required=False, strip=True)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Mot de passe', min_length=8, widget=forms.PasswordInput(), required=True)
    # password_confirm = forms.CharField(label='Confirmer le mot de passe', min_length=8, widget=forms.PasswordInput(), required=True)  
    job=forms.ChoiceField(label='Métier', choices=JOBS, initial='python',required=True) 
    cpu_accept=forms.BooleanField(label='Accepter les cookies', initial=True, required=True)
    
    
    def clean_pseudo(self):
        pseudo = self.cleaned_data.get('pseudo')
        if not pseudo or "$" in pseudo:
            raise forms.ValidationError("Le pseudo ne peut pas être vide ou contenir le caractère '$'.")
        return pseudo
    
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'published', 'date','author','category','description']
        labels={
            "title": "Titre",
            "content": "Contenu",
            "published": "Publication"
            
        }
        widgets = {
            "content": forms.Textarea(attrs={"rows": 5, "cols": 40}),
            "date": forms.SelectDateWidget(years=range(1990,2027)),
        }
        
class BookForm(forms.ModelForm):
    class Meta :
        model= Book
        fields= ["title","price","summary","author","category","stock"]
        labels={
            "title": "Titre",
            "price": "Prix",
            "summary": "Sommaire",
            "author": "Autheur",
            "category": "Categorie"
        }
        
   
    
