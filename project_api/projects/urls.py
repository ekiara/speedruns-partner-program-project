# projects/urls.py
from django.urls import path

from .views import ProjectListView
from .views import ProjectCreate
from .views import ProjectRetrieve
from .views import ProjectUpdate
from .views import ProjectDelete

urlpatterns = [
    path('', ProjectListView.as_view()),
    path('create/', ProjectCreate.as_view()),
    path('<int:pk>/', ProjectRetrieve.as_view()),
    path('<int:pk>/update/', ProjectUpdate.as_view()),
    path('<int:pk>/delete/', ProjectDelete.as_view()),
]
