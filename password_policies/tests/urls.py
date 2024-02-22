from django.urls import include, path, re_path

from password_policies.tests.views import TestHomeView, TestLoggedOutMixinView

urlpatterns = [
    path("password/", include("password_policies.urls")),
    re_path(r"^fubar/", TestLoggedOutMixinView.as_view(), name="loggedoutmixin"),
    path("", TestHomeView.as_view(), name="home"),
]
