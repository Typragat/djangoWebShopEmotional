from django.urls import path, re_path
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^product/(?P<product_id>\w+)', views.product),
]