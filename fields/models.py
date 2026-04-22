from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta
from django.utils import timezone


# -------------------------
# Custom User Model
# -------------------------
class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('AGENT', 'Agent'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


# -------------------------
# Field Model
# -------------------------
class Field(models.Model):
    STAGE_CHOICES = (
        ('PLANTED', 'Planted'),
        ('GROWING', 'Growing'),
        ('READY', 'Ready'),
        ('HARVESTED', 'Harvested'),
    )

    name = models.CharField(max_length=255)
    crop_type = models.CharField(max_length=255)
    planting_date = models.DateField()
    current_stage = models.CharField(max_length=20, choices=STAGE_CHOICES)
    assigned_agent = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'role': 'AGENT'}
    )

    def __str__(self):
        return self.name

    # -------------------------
    # Computed Status Logic
    # -------------------------
    @property
    def status(self):
        if self.current_stage == 'HARVESTED':
            return 'Completed'

        days_since_planting = (timezone.now().date() - self.planting_date).days

        if days_since_planting > 120 and self.current_stage != 'READY':
            return 'At Risk'

        return 'Active'


# -------------------------
# Field Updates
# -------------------------
class FieldUpdate(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='updates')
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    stage = models.CharField(max_length=20, choices=Field.STAGE_CHOICES)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.field.name} update by {self.agent.username}"