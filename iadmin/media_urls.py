from django.conf import settings
from django.conf.urls.defaults import patterns
import iadmin
import os

urlpatterns = patterns('',
                #iadmin media
                (r'^%siadmin/(?P<path>.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve',
                    {'document_root':os.path.join(os.path.abspath(os.path.dirname(iadmin.__file__)), 'media', 'iadmin'),
                     'show_indexes':True}),
                       )