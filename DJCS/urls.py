
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework_swagger.views import get_swagger_view




class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path(r'swagger/', schema_view),
    url(r'^', include(router.urls)),

]
