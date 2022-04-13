from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

from petstagram.accounts.views import ProfileView, EditProfileView, DeleteProfileView, \
    ChangeUserPasswordView, UserLogoutView
from petstagram.accounts.views import UserLoginView, UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('edit-profile/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('edit-password-done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_changed'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit profile page'),
    path('profile/delete/', DeleteProfileView.as_view(), name='delete profile page'),
]
