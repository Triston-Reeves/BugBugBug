from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class MyUser(AbstractUser):
    pass

class Ticket(models.Model):
    title = models.TextField(max_length=80, default="")
    description = models.CharField(max_length=240)
    time_date = models.DateTimeField(default=timezone.now)
    assigned_to = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='assigned_to', blank=True, null=True)
    completed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='completed_by', blank=True, null=True)
    ticket_master = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='ticket_master')
    New = "N"
    In_progress = "P"
    Done = "D"
    Invalid = "I"
    STATUS_CHOICES = [
        (New, "New"),
        (In_progress, "In Progress"),
        (Done, "Done"),
        (Invalid, "Invalid")
    ]
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=New
    )


