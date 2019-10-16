from rest_framework import routers
from sport.viewsets import ReservationViewSet, FieldViewSet, CompanyViewSet
from sport import views
from django.urls import path


router = routers.SimpleRouter()
router.register('reservations', ReservationViewSet)
router.register('fields', FieldViewSet)
router.register('companies', CompanyViewSet)
urlpatterns = router.urls