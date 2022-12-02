from django.urls import path
from . import views

urlpatterns = [
    path("",views.SchemaCreateList.as_view())
]
