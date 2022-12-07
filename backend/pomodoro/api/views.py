from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import generics
from .serializers import SchemaSerializer, CategorySerializer, PomodoroSerializer, UserSerializer
from timetracker.models import Schema, Category, Pomodoro
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework import permissions

# Create your views here.

class CreateUserView(generics.CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer


class SchemaCreateList(generics.ListCreateAPIView):
    serializer_class = SchemaSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Schema.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SchemaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
    
    def perform_update(self, serializer):
        active = serializer.validated_data.get("active")
        if active == True:
            Schema.objects.all().update(active=False)
        isinstance = serializer.save(active=active)

class CategoryCreateList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Category.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

    def perform_update(self, serializer):
        isinstance = serializer.save()

class PomodoroCreateList(generics.ListCreateAPIView):
    serializer_class = PomodoroSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Pomodoro.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PomodoroRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pomodoro.objects.all()
    serializer_class = PomodoroSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

    def perform_update(self, serializer):
        isinstance = serializer.save()

@api_view(['POST'])
def pomodoro_amount(request,id):
    pomodoro = Pomodoro.objects.filter(id = id).first()
    amount = pomodoro.amount
    if amount > 0:
        amount -= 1
        if amount == 0:
            done = True
            pomodoro.amount = amount
            pomodoro.done = True
            pomodoro.save()
        else:
            pomodoro.amount = amount
            pomodoro.save()
        context = {"id":pomodoro.id,"category_id": pomodoro.category_id.id,"title":pomodoro.title,"amount":pomodoro.amount,"done":pomodoro.done,}
        return Response(context)
    else:
        context = {"id":pomodoro.id,"category_id": pomodoro.category_id.id,"title":pomodoro.title,"amount":pomodoro.amount,"done":pomodoro.done,}
        return Response(context)
