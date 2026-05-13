
from django.urls import path
from . import views

urlpatterns = [
    path('profile/manage', views.manageProfle,name="manage-profile"),
    path('profile/recent-booking', views.recentBooking,name="recent-booking"),
]
