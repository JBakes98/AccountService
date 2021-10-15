from django.contrib import admin
from django.urls import path
from account.views import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', api.RegisterView.as_view(), name='register'),
    path('login/', api.LoginView.as_view(), name='login'),
    path('logout/', api.LogoutView.as_view(), name='logout'),
    path('detail/', api.UserDetailsView.as_view(), name='user_detail'),
    path('verification/confirm/<str:uidb64>/<str:token>/', api.AccountVerifyConfirmView.as_view(),
         name='account_verify_confirm'),

    path('password/change/', api.PasswordChangeView.as_view(), name='password_change'),
    path('password/reset/', api.PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/<str:uidb64>/<str:token>/', api.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
]
