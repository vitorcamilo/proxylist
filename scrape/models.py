from django.db import models
from django.urls import reverse_lazy


class IPlist(models.Model):
    ipadress = models.CharField(max_length=20, null=False, blank=False)
    port = models.CharField(max_length=4, null=True)
    protocol = models.CharField(max_length=5, null=True)
    anonymity = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=30, null=True)
    region = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)
    uptime = models.CharField(max_length=6)
    runtime = models.CharField(max_length=4)
    transfer = models.CharField(max_length=4)

    class Meta:
        app_label = 'scrape'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse_lazy('index')
