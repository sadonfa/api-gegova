from rest_framework.serializers import ModelSerializer
from about.models import About


class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title', 'info', 'icono')
