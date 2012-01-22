from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
import models
import logging
from django.shortcuts import render_to_response

def home(request):
    """ basic homepage view """
    template_vars = {}
    template_vars['test'] = 'test'

    if request.POST.get('add_post'):
        blog_post_form = models.BlogPostForm(request.POST)
        if blog_post_form.is_valid():
            blog_post_form.save()
            return HttpResponseRedirect('/');
    else:
        blog_post_form = models.BlogPostForm()

    if request.POST.get('add_user'):
        user_form = models.UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect('/');
    else:
        user_form = models.UserForm()

    if request.POST.get('add_category'):
        category_form = models.BlogCategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect('/');
    else:
        category_form = models.BlogCategoryForm()

    template_vars['blog_post_form'] = blog_post_form
    template_vars['user_form'] = user_form
    template_vars['category_form'] = category_form


    template_vars['posts'] = models.BlogPost.objects.all()
    return render_to_response("home.html", template_vars, RequestContext(request))