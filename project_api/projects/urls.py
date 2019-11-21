# projects/urls.py
from django.urls import path

from .views import ProjectListView
from .views import ProjectCreate
from .views import ProjectRetrieve
from .views import ProjectUpdate
from .views import ProjectDelete

urlpatterns = [
    path(route='', view=ProjectListView.as_view(), name="projects_root"),
    path(route='create/', view=ProjectCreate.as_view(), name="projects_create"),
    path(route='<int:pk>/', view=ProjectRetrieve.as_view(), name="projects_retrieve"),
    path(route='<int:pk>/update/', view=ProjectUpdate.as_view(), name="projects_update"),
    path(route='<int:pk>/delete/', view=ProjectDelete.as_view(), name="projects_delete"),
]
