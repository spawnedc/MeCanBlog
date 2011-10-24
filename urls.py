from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^(?P<study_class_name>custom_study|third_party_study)/create$', 'mecanblog.views.home'),
    (r'^$', 'mecanblog.views.home'),
)
