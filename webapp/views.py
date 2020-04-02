from typing import List

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from webapp.models import RedisServer

CRUD_FIELDS: List[str] = ["name", "host", "password", "port", "db"]


class ServerCreate(CreateView):
    model = RedisServer
    fields = CRUD_FIELDS


class ServerUpdate(UpdateView):
    model = RedisServer
    fields = CRUD_FIELDS
    template_name_suffix = "_update_form"


class ServerDelete(DeleteView):
    model = RedisServer
    success_url = reverse_lazy("home-page")
