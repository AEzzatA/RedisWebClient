from django.urls import path

from webapp import views


urlpatterns = [
    path("create_server/", views.ServerCreate.as_view(), name="ServerCreate"),
    path("update_server/<pk>/", views.ServerUpdate.as_view(), name="ServerUpdate"),
    path("delete_server/<pk>/", views.ServerUpdate.as_view(), name="ServerDelete"),
    path("", views.ServerIndex.as_view(), name="ServerIndex"),
]
