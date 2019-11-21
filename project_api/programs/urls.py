# partners/urls.py
from django.urls import include
from django.urls import path

from .views import ProgramListView
from .views import ProgramCreate
from .views import ProgramRetrieve
from .views import ProgramUpdate
from .views import ProgramDelete

urlpatterns = [
    path(route='', view=ProgramListView.as_view(), name="programs_root"),
    path(route='create/', view=ProgramCreate.as_view(), name="programs_create"),
    path(route='<int:pk>/', view=ProgramRetrieve.as_view(), name="programs_retrieve"),
    path(route='<int:pk>/update/', view=ProgramUpdate.as_view(), name="programs_update"),
    path(route='<int:pk>/delete/', view=ProgramDelete.as_view(), name="programs_delete"),
]
