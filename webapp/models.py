from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class RedisServer(models.Model):
    name = models.CharField(
        max_length=255, help_text=_("A name to identify the server")
    )

    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    host = models.CharField(max_length=255)
    port = models.CharField(max_length=4)
    password = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse("server-info", kwargs={"pk": self.pk})

    def __str__(self):
        return name
