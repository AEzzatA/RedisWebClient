from typing import List

from django.urls import reverse_lazy
from django.db.models import QuerySet
from django.views import generic
from webapp.models import RedisServer

CRUD_FIELDS: List[str] = ["name", "host", "password", "port", "db"]


class ServerIndex(generic.ListView):
    template_name = "webapp/homepage.html"
    context_object_name = "servers"
    queryset: QuerySet = RedisServer.objects.all()


class ServerCreate(generic.CreateView):
    template_name = "webapp/create_server.html"
    model = RedisServer
    fields = CRUD_FIELDS
    success_url = reverse_lazy("webapp:ServerIndex")


class ServerDetail(generic.DeleteView):
    model = RedisServer
    context_object_name = "server"
    template_name = "webapp/server_detail.html"


class ServerUpdate(generic.UpdateView):
    model = RedisServer
    fields = CRUD_FIELDS
    template_name_suffix = "_update_form"


class ServerDelete(generic.DeleteView):
    model = RedisServer
    success_url = reverse_lazy("home-page")


class Connect(generic.View):
    def get(self, request, **kwargs):
        return
