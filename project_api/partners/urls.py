# partners/urls.py
from django.urls import include
from django.urls import path

from .views import PartnerListView
from .views import PartnerCreate
from .views import PartnerRetrieve
from .views import PartnerUpdate
from .views import PartnerDelete

urlpatterns = [
    path(route="", view=PartnerListView.as_view(), name="partners_root"),
    path(route="create/", view=PartnerCreate.as_view(), name="partners_create"),
    path(route="<int:pk>/", view=PartnerRetrieve.as_view(), name="partners_retrieve"),
    path(route="<int:pk>/update/", view=PartnerUpdate.as_view(), name="partners_update"),
    path(route="<int:pk>/delete/", view=PartnerDelete.as_view(), name="partners_delete"),
]
