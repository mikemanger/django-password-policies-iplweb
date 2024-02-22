from django.urls import path, re_path

try:
    # patterns was deprecated in Django 1.8
    from django.conf.urls import patterns
except ImportError:
    # patterns is unavailable in Django 1.10+
    patterns = False

from password_policies import views

urlpatterns = [
    path(
        "change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("change/", views.PasswordChangeFormView.as_view(), name="password_change"),
    path("reset/", views.PasswordResetFormView.as_view(), name="password_reset"),
    path(
        "reset/complete/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    re_path(
        r"^reset/confirm/([0-9A-Za-z_\-]+)/([0-9A-Za-z]{1,13})/([0-9A-Za-z-=_]{1,128})/$",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/", views.PasswordResetDoneView.as_view(), name="password_reset_done"
    ),
]

if patterns:
    # Django 1.7
    urlpatterns = patterns("", *urlpatterns)
