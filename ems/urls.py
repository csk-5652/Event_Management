from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from ems import views  

urlpatterns = [
    path("", views.index,name='ems'),
    path("login/",views.loginUser,name='loginUser'),
    path("logout/",views.logoutUser, name="logoutUser"),
    path("register/",views.registerUser,name='registerUser'),
    path("eventsview/",views.eventsview,name='eventsview'),
    path("news/",views.news,name='news'),
    path("booking/",views.booking,name='booking'),
    path("delete_booking/<int:id>/",views.delete_booking,name='delete_booking'),
    path("bookform/<int:id>",views.bookform,name='bookform'),
    path("profile/",views.profile,name="profile"),
    path("edit_profile/",views.edit_profile,name="edit_profile"),
    

    # password reset 
    path("reset_password/",auth_views.PasswordResetView.as_view(),name='reset_password'),
    path("reset_password_Sent/",auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path("reset_password_complete/",auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    # admin panel 
    path("manage/",views.manage,name='manage'),

]
