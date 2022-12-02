from rest_framework import generics
from .serializers import SchemaSerializer
from timetracker.models import Schema

# Create your views here.

class SchemaCreateList(generics.ListCreateAPIView):
    serializer_class = SchemaSerializer

    def get_queryset(self):
        return Schema.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)