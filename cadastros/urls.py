from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = "cadastros"

urlpatterns = [
    path("", views.VagaListView.as_view(), name="list"),
    path("<slug:slug>/", views.VagaDetailView.as_view(), name="detail"),
]