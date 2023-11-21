from django.urls import include, path
from rest_framework import routers
from shortener import views

router = routers.DefaultRouter()
router.register(r"", views.ShortnerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
