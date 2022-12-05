from rest_framework import generics
from .serializers import SchemaSerializer, CategorySerializer, PomodoroSerializer, PomodoroAmountSerializer
from timetracker.models import Schema, Category, Pomodoro
from rest_framework.response import Response

# Create your views here.

class SchemaCreateList(generics.ListCreateAPIView):
    serializer_class = SchemaSerializer

    def get_queryset(self):
        return Schema.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SchemaUpdate(generics.RetrieveUpdateAPIView):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        isinstance = serializer.save()

class SchemaDelete(generics.RetrieveDestroyAPIView):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

class SchemaDetail(generics.RetrieveAPIView):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer
    lookup_field = "pk"

class CategoryCreateList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

    def perform_update(self, serializer):
        isinstance = serializer.save()

class PomodoroCreateList(generics.ListCreateAPIView):
    serializer_class = PomodoroSerializer

    def get_queryset(self):
        return Pomodoro.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PomodoroRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pomodoro.objects.all()
    serializer_class = PomodoroSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

    def perform_update(self, serializer):
        isinstance = serializer.save()

class PomodoroUpdateAmount(generics.RetrieveUpdateAPIView):
    queryset = Pomodoro.objects.all()
    serializer_class = PomodoroAmountSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        done = serializer.validated_data.get("done")
        amount = serializer.validated_data.get("amount")
        if amount == 0:
            done = True
            serializer.save(done=done, amount=amount)
        elif amount < 0:
            return Response({"Invalid":"amount can not be less than 0"}, status=400)
        else:
            done = False
            serializer.save(done=done, amount=amount)
        

