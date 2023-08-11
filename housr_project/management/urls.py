from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.homepage, name='homepage'),
    path('management/manage-permissions/', views.manage_permissions, name='manage_permissions'),

]
