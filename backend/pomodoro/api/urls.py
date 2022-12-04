from django.urls import path
from . import views

urlpatterns = [
    path("schema/",views.SchemaCreateList.as_view()),
    path("schema/<int:pk>/",views.SchemaDetail.as_view()),
    path("schema/<int:pk>/update",views.SchemaUpdate.as_view()),
    path("schema/<int:pk>/delete",views.SchemaDelete.as_view()),
    path("category/",views.CategoryCreateList.as_view()),
    path("category/<int:pk>/",views.CategoryRetrieveUpdateDestroy.as_view()),
]
