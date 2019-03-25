from django.conf.urls import url

from . views import( post_model_list_view,

                     post_model_create_view,
                     post_model_update_view,
                     post_model_delete_view
                     )




urlpatterns = [

    url(r'^$', post_model_list_view, name='list'),
    url(r'^create/$', post_model_create_view, name='create'),
    url(r'^(?P<id>\d+)/edit/$', post_model_update_view, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_model_delete_view, name='delete'),
]