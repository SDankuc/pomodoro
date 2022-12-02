from rest_framework import generics
from .serializers import SchemaSerializer
from timetracker.models import Schema

# Create your views here.

class SchemaList(generics.ListAPIView):
    serializer_class = SchemaSerializer

    def get_queryset(self):
        return Schema.objects.all()