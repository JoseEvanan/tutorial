from django.conf.urls import url, include
from rest_framework import routers
from quickstart.views import UserViewSet, GroupViewSet
from quickstart.views import StudentViewSet, UniversityViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]