from django.db import models
from django.core.validators import RegexValidator
from rest_framework.exceptions import ValidationError


phone_validator = RegexValidator(regex=r"^01[0-2,5]{1}[0-9]{8}$", message="Enter a valid number!")
linkedIn_validator = RegexValidator(regex=r"^https://linkedin.com/", message="Enter a valid linkedIn url!")
github_validator = RegexValidator(regex=r"^https://github.com/", message="Enter a valid github url!")

# Create your models here.
class Candidate(models.Model):
    first_name = models.CharField(max_length=20, null=False, verbose_name="First name")
    last_name = models.CharField(max_length=20, null=False, verbose_name="Last name")
    email = models.EmailField(max_length=50, null=False)
    phone_number = models.CharField(max_length=11, validators=[phone_validator])
    preferred_time_start = models.TimeField(null=False)
    preferred_time_end = models.TimeField(null=False)
    linkedIn = models.URLField(null=False, validators=[linkedIn_validator])
    github = models.URLField(null=False, validators=[github_validator])
    comment = models.TextField(null=False)

    def clean(self):
        if self.preferred_time_end <= self.preferred_time_start:
            raise ValidationError({"Time": ["End time must be after start time!"]})

    def __str__(self):
        return f"{self.email}"