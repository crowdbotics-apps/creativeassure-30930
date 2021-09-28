from django.conf import settings
from django.db import models


class Usertype(models.Model):
    "Generated Model"
    usertype = models.CharField(
        max_length=256,
    )
