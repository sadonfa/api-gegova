from rest_framework.viewsets import ModelViewSet
from about.models import About
from about.api.serializers import AboutSerializer


class AboutApiViewSet(ModelViewSet):
    serializer_class = AboutSerializer
    queryset = About.objects.all()
