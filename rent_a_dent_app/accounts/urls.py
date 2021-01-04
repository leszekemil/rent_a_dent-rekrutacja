from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path, include
from accounts.views import MyLoginView, SingUpView, CreateUser, ChangePermissionView, UserListView
from accounts import views


urlpatterns = [
    path("", include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('myLogin/', views.MyLoginView.as_view(), name='myLoginView'),
    path('signUp/', views.SingUpView.as_view(), name='SingUpView'),
    path('create_user/', views.CreateUser.as_view(), name='create_user'),
    path('change_permission/<int:pk>', views.ChangePermissionView.as_view(), name='change_permission'),
    path('user_list/', views.UserListView.as_view(), name='user_list'),
    path('profile/', views.UserListView.as_view(), name='profile'),
    path('logout/', views.logout, name='logout')
]
