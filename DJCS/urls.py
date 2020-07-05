

#from  Login.views import Login  
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include
from django.contrib.auth.models import User


from rest_framework import routers,serializers,viewsets
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^',include(router.urls)),
    url('swagger/', schema_view),
    """re_path(r'^appi/v1/login',include('Login.urls')), 
    re_path(r'^appi/v1/example1',include('Example1.urls')), 
    re_path(r'^appi/v1/example2',include('Example2.urls')), 
    re_path(r'^appi/v1/registro',include('Registro.urls')),"""
] 