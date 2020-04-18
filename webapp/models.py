from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify


class RedisServer(models.Model):
    name = models.CharField(
        max_length=255, unique=True, help_text=_("A name to identify the server")
    )
    host = models.CharField(max_length=255, help_text=_("redis server host"))
    port = models.PositiveIntegerField(default=6379, help_text=_("redis server port"))
    password = models.CharField(max_length=255, help_text=_("redis server host"))
    db = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse("server-info", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.name
