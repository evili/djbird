from django.conf.urls import url
from .views import SpeciesListView, GenusListView

urlpatterns = [
    url(r'^species/$', SpeciesListView.as_view()),
    url(r'^clades/$', GenusListView.as_view())
]
