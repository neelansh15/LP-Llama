from django.conf.urls import include
from django.urls import re_path

from lp_lama import views
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()

schema_view = get_swagger_view(title='Code Review Tools APIs')

urlpatterns = [
    re_path(r'^docs/', schema_view),
    re_path(r'^', include(router.urls)),
]