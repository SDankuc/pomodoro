from django.urls import path
from . import views
from rest_framework_simplejwt.views import(TokenObtainPairView,TokenRefreshView,TokenVerifyView)

urlpatterns = [
    path("schema/",views.SchemaCreateList.as_view()),
    path("token/",TokenObtainPairView.as_view(), name = "token_obtain_pair"),
    path("token/refresh/",TokenRefreshView.as_view(), name = "token_refresh"),
    path("token/verify/",TokenVerifyView.as_view(), name = "token_verify"),
    path("schema/<int:pk>/",views.SchemaDetail.as_view()),
    path("schema/<int:pk>/update",views.SchemaUpdate.as_view()),
    path("schema/<int:pk>/delete",views.SchemaDelete.as_view()),
    path("category/",views.CategoryCreateList.as_view()),
    path("category/<int:pk>/",views.CategoryRetrieveUpdateDestroy.as_view()),
    path("pomodoro/",views.PomodoroCreateList.as_view()),
    path("pomodoro/<int:pk>/",views.PomodoroRetrieveUpdateDestroy.as_view()),
    path("pomodoro/<int:pk>/amount",views.PomodoroUpdateAmount.as_view()),
]
