from django.contrib.auth.views import LoginView
from .views import MyLogout, AboutMeView, RegisterView
from django.urls import path

app_name = "myauth"

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'shop_auth/login.html', redirect_authenticated_user=True), name ="login"),
    path('logout/', MyLogout.as_view(), name='logout'),
    path('about-user/', AboutMeView.as_view(), name='about-user'),
    path('register/', RegisterView.as_view(), name='register'),
]