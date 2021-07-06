from django.urls import path,include
from .forms import LoginForm
from re import template
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/signin.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('',views.SignUpView.as_view(),name='signup'),
    path('task/',views.task,name='task'),
    path('viewtask/',views.viewtask,name='viewtask'),
    path('hierarchy/',views.hierarchy,name='hierarchy'),
    path('showhierarchy/',views.showhierarchy,name='showhierarchy'),




]