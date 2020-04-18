from typing import List

from django.urls import reverse_lazy
from django.views import generic
from webapp.models import RedisServer

CRUD_FIELDS: List[str] = ["name", "host", "password", "port", "db"]


class ServerIndex(generic.ListView):
    template_name = "webapp/servers_index.html"
    context_object_name = "servers"
    queryset = RedisServer.objects.all()


class ServerCreate(generic.CreateView):
    template_name = "webapp/create_server.html"
    model = RedisServer
    fields = CRUD_FIELDS


class ServerUpdate(generic.UpdateView):
    model = RedisServer
    fields = CRUD_FIELDS
    template_name_suffix = "_update_form"


class ServerDelete(generic.DeleteView):
    model = RedisServer
    success_url = reverse_lazy("home-page")
