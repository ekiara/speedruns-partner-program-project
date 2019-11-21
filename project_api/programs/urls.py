# partners/urls.py
from django.urls import include
from django.urls import path

from .views import ProgramListView
from .views import ProgramCreate
from .views import ProgramRetrieve
from .views import ProgramUpdate
from .views import ProgramDelete

urlpatterns = [
    path('', ProgramListView.as_view()),
    path('create/', ProgramCreate.as_view()),
    path('<int:pk>/', ProgramRetrieve.as_view()),
    path('<int:pk>/update/', ProgramUpdate.as_view()),
    path('<int:pk>/delete/', ProgramDelete.as_view()),
]
