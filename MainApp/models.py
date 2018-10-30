
from django.db import models


class WishList(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    url = models.URLField()
    post = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return self.title