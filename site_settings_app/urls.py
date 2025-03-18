from django.urls import path
from site_settings_app.views import (
    settings_api_view,
    about_api_view,
    contact_api_view,
    notification_api_view,
)

urlpatterns = [
    path(
        "",
        settings_api_view,
        name="settings_api_view",
    ),
    path(
        "about/",
        about_api_view,
        name="about_api_view",
    ),
    path(
        "contact/",
        contact_api_view,
        name="contact_api_view",
    ),
    path(
        "notification/",
        notification_api_view,
        name="notification_api_view",
    ),
]
