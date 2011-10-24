from django.db import models
from django import forms

class ModelBase(models.Model):
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)
    
    class Meta:
        abstract = True
        
class User(ModelBase):
    username = models.CharField(max_length=100)
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
    
class BlogCategory(ModelBase):
    title = models.CharField(max_length=100)
    
class BlogCategoryForm(forms.ModelForm):
    class Meta:
        model = BlogCategory

class BlogPost(ModelBase):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    url_slug = models.TextField(max_length=100, blank=True)
    category = models.ForeignKey(BlogCategory)
    user = models.ForeignKey(User)
    
    
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        
    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)
        self.fields['category'].choices = [(bc.id, bc.title) for bc in BlogCategory.objects.all()]
        self.fields['user'].choices = [(u.id, u.username) for u in User.objects.all()]