from rest_framework.routers import DefaultRouter
from portafolio.api.views import PortafolioApiViewSet

router_portafolio = DefaultRouter()


router_portafolio.register(
    prefix='portafolio', basename='portafolio', viewset=PortafolioApiViewSet
)
