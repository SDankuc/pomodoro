from rest_framework import generics
from .serializers import SchemaSerializer, CategorySerializer
from timetracker.models import Schema, Category

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