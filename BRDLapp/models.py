from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True)
    slug = models.SlugField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']


class SopaForm(models.Model):
    fname = models.CharField(max_length=255, null=True)
    mname = models.CharField(max_length=255, null=True)
    lname = models.CharField(max_length=255, null=True)
    company_name = models.CharField(max_length=255, null=True)
    Identification = models.IntegerField()
    mobile_tel = models.IntegerField()
    office_tel = models.IntegerField()
    email = models.EmailField()
    postal_address = models.CharField(max_length=255)
    lawyers = models.CharField(max_length=255)
    referred_by = models.CharField(max_length=255)

    date_added = models.DateTimeField(auto_now_add=True)


OPTION_CHOICES = (
    ("1", "One"),
    ("2", "Two")
)


def number_validator(value):
    if len(value) < 10:
        raise ValidationError(
            _("%(value)s is not a correct phone number"),
            params={"value": value},
        )

class OlengaiForm(models.Model):
    fname = models.CharField(max_length=255, null=True)
    mname = models.CharField(max_length=255, null=True)
    lname = models.CharField(max_length=255, null=True)
    company_name = models.CharField(max_length=255, null=True)
    Identification = models.IntegerField()
    mobile_tel = models.IntegerField()
    office_tel = models.IntegerField()
    email = models.EmailField()
    postal_address = models.CharField(max_length=255)
    lawyers = models.CharField(max_length=255)
    referred_by = models.CharField(max_length=255)

    date_added = models.DateTimeField(auto_now_add=True)
 

