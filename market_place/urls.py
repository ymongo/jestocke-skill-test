from django.urls import path
from .views import StorageBoxView, FilteredStorageBoxListView
from . import views

urlpatterns = [
    path("", FilteredStorageBoxListView.as_view(), name="index"),
]