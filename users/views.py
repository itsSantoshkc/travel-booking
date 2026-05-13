from django.shortcuts import render

# Create your views here.
def manageProfle(request):
    return render(request,"users/profile/manage_profile.html")

def recentBooking(request):
    return render(request,"users/profile/recent_booking.html")