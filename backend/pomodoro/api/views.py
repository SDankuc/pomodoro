from rest_framework import generics
from .serializers import SchemaSerializer, CategorySerializer, PomodoroSerializer, PomodoroAmountSerializer
from timetracker.models import Schema, Category, Pomodoro
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.


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

class PomodoroUpdateAmount(generics.RetrieveUpdateAPIView):
    queryset = Pomodoro.objects.all()
    serializer_class = PomodoroAmountSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "pk"

    def perform_update(self, serializer):
        done = serializer.validated_data.get("done")
        amount = serializer.validated_data.get("amount")
        if amount == 0:
            done = True
            serializer.save(done=done, amount=amount)
        elif amount < 0:
            return Response({"Invalid": "amount can not be less than 0"}, status=400)
        else:
            done = False
            serializer.save(done=done, amount=amount)
