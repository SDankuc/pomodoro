from django.urls import path
from . import views
from rest_framework_simplejwt.views import(TokenObtainPairView,TokenRefreshView,TokenVerifyView)

urlpatterns = [
    path("token/",TokenObtainPairView.as_view(), name = "token_obtain_pair"),
    path("token/refresh/",TokenRefreshView.as_view(), name = "token_refresh"),
    path("token/verify/",TokenVerifyView.as_view(), name = "token_verify"),
    path("schemas/",views.SchemaCreateList.as_view()),
    path("schema/<int:pk>/",views.SchemaRetrieveUpdateDestroy.as_view()),
    path("categories/",views.CategoryCreateList.as_view()),
    path("category/<int:pk>/",views.CategoryRetrieveUpdateDestroy.as_view()),
    path("pomodoros/",views.PomodoroCreateList.as_view()),
    path("pomodoro/<int:pk>/",views.PomodoroRetrieveUpdateDestroy.as_view()),
    path("pomodoro/<id>/amount",views.pomodoro_amount),
]
