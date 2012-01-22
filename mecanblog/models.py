from django.db import models
from django import forms
from google.appengine.api import users
import logging
import re

class ModelBase(models.Model):
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        abstract = True

    def slugify(self, attr):
        removelist = ["a", "an", "as", "at", "before", "but", "by", "for", "from", "is", "in", "into", "like", "of", "off", "on", "onto", "per", "since", "than", "the", "this", "that", "to", "up", "via", "with"];
        for a in removelist:
            aslug = re.sub(r'\b' + a + r'\b', '', getattr(self, attr))
        aslug = re.sub('[^\w\s-]', '', aslug).strip().lower()
        aslug = re.sub('\s+', '-', aslug)
        return aslug

class User(ModelBase):
    email = models.CharField(max_length=100)

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
    category = models.ForeignKey(BlogCategory)
    content = models.TextField()
    slug = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User)

    def slugify_url_slug(self):
        self.slug = self.slugify('title')


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ['slug', 'user', ]

    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)
        self.fields['category'].choices = [(bc.id, bc.title) for bc in BlogCategory.objects.all()]

    def save(self, *args, **kwargs):
        model = super(BlogPostForm, self).save(commit=False)
        current_user = users.get_current_user()
        user, created = User.objects.get_or_create(email=current_user.email())
        model.user = user
        model.slugify_url_slug()
        model.save()
        return model

