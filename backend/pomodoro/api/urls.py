from django.urls import path
from . import views

urlpatterns = [
    path("",views.SchemaList.as_view())
]
