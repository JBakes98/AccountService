from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('detail/', views.UserDetailsView.as_view(), name='user_detail'),
    path('verification/confirm/<str:uidb64>/<str:token>/', views.AccountVerifyConfirmView.as_view(),
         name='account_verify_confirm'),

    path('password/change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password/reset/', views.PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/<str:uidb64>/<str:token>/', views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
]
