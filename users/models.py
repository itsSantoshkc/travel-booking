import uuid
from django.db import models


class User(models.Model):
    userID = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=15, blank=True, null=True)
    dateOfBirth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

