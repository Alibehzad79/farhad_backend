from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from accounts_app.views import (
    register_api_view,
    send_reset_password_email_api_view,
    change_password_api_view,
    user_detail_api_view,
    edit_user_detail_api_view,
)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    #########
    path("register/", register_api_view, name="register_api_view"),
    path(
        "send-reset-password-email/",
        send_reset_password_email_api_view,
        name="send_reset_password_email_api_view",
    ),
    path(
        "change-password/",
        change_password_api_view,
        name="change_password_api_view",
    ),
    path("user/", user_detail_api_view, name="user_detail_api_view"),
    path("user/edit/", edit_user_detail_api_view, name="edit_user_detail_api_view"),
]
