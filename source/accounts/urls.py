from django.urls import path
from accounts.views import login_view, logout_view, register_view, UserDetailView, UserPersonalInfoChangeView, \
    UserPasswordChangeView


urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("create", register_view, name="create"),
    path("<int:pk>/", UserDetailView.as_view(), name="detail"),
    path("<int:pk>/update", UserPersonalInfoChangeView.as_view(), name="update"),
    path("<int:pk>/change_password", UserPasswordChangeView.as_view(), name="change_password")

]

app_name = "accounts"

