from rest_framework.viewsets import ModelViewSet
from portafolio.models import Portafolio
from portafolio.api.serializers import PortafolioSerializer


class PortafolioApiViewSet(ModelViewSet):
    serializer_class = PortafolioSerializer
    queryset = Portafolio.objects.all()
