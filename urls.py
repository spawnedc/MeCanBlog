from django.conf.urls.defaults import patterns, url, include

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    url('^_ah/warmup$', 'djangoappengine.views.warmup'),
    
    url(r'^', include('mecanblog.urls')),
)
