# movies-api/movies/api/urls.py

from api.views import MovieCreateView, MovieDetailView
from django.conf.urls import url

urlpatterns = [
    url(r'^movies/$', MovieCreateView.as_view(), name='movies'),
    url(r'^movies/(?P<id>[0-9]+)$', MovieDetailView.as_view(), name='detail'),
]
