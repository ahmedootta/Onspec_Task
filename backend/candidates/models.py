from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify

phone_validator = RegexValidator(regex=r"^01[0-2,5]{1}[0-9]{8}$", message="Enter a valid number!")

# Create your models here.
class Candidate(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="First name")
    last_name = models.CharField(max_length=20, verbose_name="Last name")
    slug = models.SlugField(unique=True, blank=True)
    email = models.EmailField(max_length=50, unique=True) # unique field indexed by default
    phone_number = models.CharField(max_length=11, validators=[phone_validator])
    preferred_time_start = models.TimeField()
    preferred_time_end = models.TimeField()
    linkedIn = models.URLField()
    github = models.URLField()
    comment = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.email}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email}"