from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Address(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address_line = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s" % str(self.id)














