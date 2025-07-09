from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WindDataViewSet, wind_test, all_wind_data, wind_data_by_max_speed

router = DefaultRouter()
router.register(r'winddata', WindDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('test/', wind_test, name='wind_test'),
    path('wind/all/', all_wind_data, name='all_wind_data'),
    path('wind/max-speed/<str:max_speed>/', wind_data_by_max_speed, name='wind_data_by_max_speed'),
]