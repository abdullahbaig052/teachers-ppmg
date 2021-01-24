from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class BaseModel(models.Model):
    """Provide default fields that are expectedly to be needed by almost all models"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class TeachersModel(BaseModel):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    profile_picture = models.CharField(max_length=256, null=True)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(help_text="Provide phone number in international format")
    room_number = models.CharField(max_length=4, null=True)
    subjects_taught = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'