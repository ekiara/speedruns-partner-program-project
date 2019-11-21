# partners/urls.py
from django.urls import include
from django.urls import path

from .views import PartnerListView
from .views import PartnerCreate
from .views import PartnerRetrieve
from .views import PartnerUpdate
from .views import PartnerDelete

urlpatterns = [
    path('', PartnerListView.as_view()),
    path('create/', PartnerCreate.as_view()),                                   
    path('<int:pk>/', PartnerRetrieve.as_view()),                               
    path('<int:pk>/update/', PartnerUpdate.as_view()),                          
    path('<int:pk>/delete/', PartnerDelete.as_view()),                          
]
