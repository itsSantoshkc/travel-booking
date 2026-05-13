from django.shortcuts import get_object_or_404, render

from travel_packages.models import TravelPackage

# Create your views here.
def index(request):
    packages = TravelPackage.objects.prefetch_related('images').all()
    return render(request,"travel_packages/index.html",{'packages': packages})


def packageDetails(request, id):
    package = get_object_or_404(
        TravelPackage.objects.prefetch_related('images'),
        package_id=id
    )
    available_slots = package.totalSlots 
    return render(request, 'travel_packages/package_detail.html', {
        'package': package,
        'available_slots': available_slots,
    })

def searchPackage(request):
    package_query = request.GET.get("t", "").strip()
    
    packages = (
        TravelPackage.objects.prefetch_related('images').filter(name__istartswith=package_query)
        if package_query
        else TravelPackage.objects.prefetch_related('images').all()
    )


    return render(request, 'travel_packages/package_search.html', {
        'packages': packages,
        'query': package_query,
    })