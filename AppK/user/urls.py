from rest_framework import routers
from user.viewsets import CustomerViewSet
from user import views
from django.urls import path


router = routers.SimpleRouter()
router.register('customers', CustomerViewSet)
urlpatterns = router.urls