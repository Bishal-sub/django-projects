from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView,LoginView


urlpatterns = [
    path('',views.home,name='home'),
    path('logout/',LogoutView.as_view(next_page = 'login'),name='logout'),
    path('login/',LoginView.as_view(next_page = 'login'),name='login'),

]
