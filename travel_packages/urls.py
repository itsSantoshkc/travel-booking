
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="homepage"),
    path('package/<uuid:id>/', views.packageDetails, name="packageDetails"),
    path('search/', views.searchPackage, name="searchPackages"),
]
