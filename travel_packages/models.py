import uuid
from django.db import models


class TravelPackage(models.Model):
    package_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    arrivalTime = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(blank=True, null=True)
    starting_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    totalSlots = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class PackageImage(models.Model):
    image_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    package = models.ForeignKey(
        TravelPackage,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image_path = models.CharField(max_length=255)

    def __str__(self):
        return f"Image for {self.package.name}"