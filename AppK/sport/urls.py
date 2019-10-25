from rest_framework import routers
from sport.viewsets import ReservationViewSet, FieldViewSet, CompanyViewSet, DoReservationViewSet, ScheduleViewSet
from sport import views
from django.urls import path


router = routers.SimpleRouter()
router.register('reservations', ReservationViewSet)
router.register('do-reservation', DoReservationViewSet)
router.register('fields', FieldViewSet)
router.register('companies', CompanyViewSet)
router.register('schedules', ScheduleViewSet)
urlpatterns = router.urls