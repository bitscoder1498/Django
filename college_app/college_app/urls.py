"""college_app URL Configuration

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
from django.contrib.auth import views as auth_views
from django.urls import path , include
from  college import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello, name = 'hello'),
    path('index/', views.index, name = 'index'),
    path('abc/', views.abc, name = 'abc'),
    path('logout/', views.logout_view, name = 'logout'),
    path('login/' , auth_views.LoginView.as_view(), name='login'),
    path('logout_new/' , auth_views.LogoutView.as_view(), name='logout'),
 ##   path('account/' , include('account.urls')),
    path('' , views.dashboard , name='dashboard'),
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
]