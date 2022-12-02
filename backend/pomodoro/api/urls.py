from django.urls import path
from . import views

urlpatterns = [
    path("schema/",views.SchemaCreateList.as_view()),
    path("schema/<int:pk>/update",views.SchemaUpdate.as_view())
]
