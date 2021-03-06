# project_api/urls.py
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.urls import re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("api.urls")),
    re_path(route="^api/v1/$", view=RedirectView.as_view(url="/api/v1/partners/", permanent=False)),
    re_path(route="^api/$", view=RedirectView.as_view(url="/api/v1/partners/", permanent=False)),
    re_path(route="^$", view=RedirectView.as_view(url="/api/v1/partners/", permanent=False)),
]
