from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from travel_packages.models import TravelPackage

def index(request):
    packages = TravelPackage.objects.prefetch_related('images').all()
    paginator = Paginator(packages, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"travel_packages/index.html",{'page_obj': page_obj})


def packageDetails(request, id):
    package = get_object_or_404(
        TravelPackage.objects.prefetch_related('images'),
        package_id=id
    )
    available_slots = package.totalSlots
    slots_range = list(range(1, available_slots + 1))
    return render(request, 'travel_packages/package_detail.html', {
        'package': package,
        'available_slots': available_slots,
        'slots_range': slots_range,
    })

def searchPackage(request):
    package_query = request.GET.get("t", "").strip()
    
    packages = (
        TravelPackage.objects.prefetch_related('images').filter(name__istartswith=package_query)
        if package_query
        else TravelPackage.objects.prefetch_related('images').all()
    )

    paginator = Paginator(packages, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'travel_packages/package_search.html', {
        'page_obj': page_obj,
        'query': package_query,
    })