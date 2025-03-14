"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from config import settings
from django.conf.urls.static import static

from azbankgateways.urls import az_bank_gateways_urls

admin.autodiscover()

api_version_v_1 = "api/v1"

urlpatterns = [
    path(f"{api_version_v_1}/accounts/", include("accounts_app.urls")),
    path(f"{api_version_v_1}/products/", include("products_app.urls")),
    path(f"{api_version_v_1}/carts/", include("carts_app.urls")),
    path(f"{api_version_v_1}/wishlist/", include("wishlist_app.urls")),
    path(f"{api_version_v_1}/orders/", include("orders_app.urls")),
    path(f"{api_version_v_1}/settings/", include("site_settings_app.urls")),
    path(f"bankgateways/", az_bank_gateways_urls()),
    path("tinymce/", include("tinymce.urls")),
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
