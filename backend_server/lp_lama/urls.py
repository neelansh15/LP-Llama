from django.conf.urls import include
from django.urls import path

from lp_lama import views
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()

schema_view = get_swagger_view(title='Code Review Tools APIs')

urlpatterns = [
    path(r'^docs/', schema_view),
    path(r'^', include(router.urls)),
]