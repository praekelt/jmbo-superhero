from django.conf.urls import patterns, include, url

from jmbo.views import ObjectDetail


urlpatterns = patterns(
    '',
    url(
        r'^(?P<slug>[\w-]+)/$',
        ObjectDetail.as_view(),
        name='superhero_object_detail'
    ),
)
