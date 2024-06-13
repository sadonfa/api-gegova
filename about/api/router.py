from rest_framework.routers import DefaultRouter
from about.api.views import AboutApiViewSet

router_about = DefaultRouter()


router_about.register(
    prefix='about', basename='about', viewset=AboutApiViewSet
)
