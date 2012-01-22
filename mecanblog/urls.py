from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('mecanblog.views',

    url(r'^post/(?P<slug>[\w-]+)/$', 'read_post_view', name="read_post_view"),
    url(r'^new_post$', 'new_post_view', name="new_post_view"),
    url(r'^$', 'home_view', name="home_view"),
   
)