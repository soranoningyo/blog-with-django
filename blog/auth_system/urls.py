from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
  path('signUp/', views.register, name="signUp" ),
  path('signIn/', auth_views.LoginView.as_view(template_name="auth_system/signIn.html"), name="signIn" ),
  path('signOut/', auth_views.LogoutView.as_view(template_name="auth_system/signOut.html"), name="signOut"),
  path('reset/', auth_views.PasswordResetView.as_view(template_name="auth_system/reset.html"), name="reset"),
  path('done-reset/', auth_views.PasswordResetDoneView.as_view(template_name="auth_system/done-reset.html"), name="done-reset"),
  path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="auth_system/confirm-reset.html"), name="password_reset_confirm"),

  path('profile/',views.profile, name="profile" ),

]
