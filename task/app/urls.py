from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetCompleteView,PasswordResetConfirmView
from django.urls import path
from . import views
from .forms import CustomPasswordResetForm

urlpatterns = [
    path('',views.signup,name="sign-up"),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('home/',views.home,name="home"),
    path('profile/',views.user_profile,name='profile'),

    path('forget-password/',views.ForgetPassword,name='forget-password'),
    path('change-password/<token>/',views.user_pass_change,name='change-password'),
]
