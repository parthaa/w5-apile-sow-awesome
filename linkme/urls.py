"""linkme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from linkworld import views
import linkworld
from django.conf.urls import url
from linkworld.backends import MyRegistrationView
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


urlpatterns = [
    path("", views.index, name="home"),
    path("data/", include("linkworld.urls")),
    path('posts/<slug>/', views.post_detail, name='post_detail'),
    path('posts/<slug>/comment/', views.comment_on_post,
         name='comment_on_post'),

    path('posts/new_post', views.new_post, name='new_post'),
    path('accounts/password/reset/', PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'), name="password_reset"),
    path('accounts/password/change/', PasswordChangeView.as_view(
        template_name='registration/password_change_form.html'), name="password_change"),
    path('accounts/password/change/done/', PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'), name="password_change_done"),
    path('accounts/password/reset/done/', PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name="password_reset_confirm"),
    path('accounts/password/done/', PasswordResetCompleteView.as_view(
         template_name='registration/password_reset_complete.html'),
         name="password_reset_complete"),
    path('accounts/register/', MyRegistrationView.as_view(),
         name='registration_register'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]
