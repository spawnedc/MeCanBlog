from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^(?P<study_class_name>custom_study|third_party_study)/create$', 'insights.views.create_study'),
    ('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
)
