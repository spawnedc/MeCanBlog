import models
from django.views.generic.base import TemplateView
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from django.views.generic.edit import BaseCreateView

class HomeView(BaseListView, TemplateView):
    template_name = "home.html"
    context_object_name = 'posts'
    model = models.BlogPost

home_view = HomeView.as_view()


class NewPostView(BaseCreateView, TemplateView):
    template_name = "create_post.html"
    form_class = models.BlogPostForm
    success_url = '/'

    def form_valid(self, *args, **kwargs):
        return super(NewPostView, self).form_valid(*args, **kwargs);

    def form_invalid(self, *args, **kwargs):
        return super(NewPostView, self).form_invalid(*args, **kwargs);

new_post_view = NewPostView.as_view()


class ReadPostView(BaseDetailView, TemplateView):
    template_name = "read_post.html"
    context_object_name = "post"
    model = models.BlogPost

read_post_view = ReadPostView.as_view()
