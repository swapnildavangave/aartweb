from django.conf.urls import url

from accounts.views import SignupView, LoginView, LogoutView, DeleteView
from accounts.views import ConfirmEmailView
from accounts.views import ChangePasswordView, PasswordResetView, PasswordResetTokenView
from accounts.views import SettingsView


urlpatterns = [
    url(r"^signup/$", SignupView.as_view(), name="account_signup"),
    url(r"^login/$", LoginView.as_view(), name="account_login"),
    url(r"^logout/$", LogoutView.as_view(), name="account_logout"),
    url(r"^confirm_email/(?P<key>\w+)/$", ConfirmEmailView.as_view(), name="account_confirm_email"),
    url(r"^password/$", ChangePasswordView.as_view(), name="account_password"),
    url(r"^password/reset/$", PasswordResetView.as_view(), name="account_password_reset"),
    url(r"^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$", PasswordResetTokenView.as_view(), name="account_password_reset_token"),
    url(r"^settings/$", SettingsView.as_view(), name="account_settings"),
    url(r"^delete/$", DeleteView.as_view(), name="account_delete"),
]
