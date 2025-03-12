from django.urls import path
from site_settings_app.views import settings_api_view

urlpatterns = [
    path(
        "",
        settings_api_view,
        name="settings_api_view",
    ),
]
