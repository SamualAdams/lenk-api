from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import WindData
from .serializers import WindDataSerializer

class WindDataViewSet(viewsets.ModelViewSet):
    queryset = WindData.objects.all()
    serializer_class = WindDataSerializer

@api_view(['GET'])
def wind_test(request):
    return Response({
        'message': 'Wind API is working!',
        'data': {
            'name': 'Test Wind Station',
            'speed': 15.5,
            'direction': 'NW'
        }
    })

@api_view(['GET'])
def all_wind_data(request):
    wind_data = WindData.objects.all()
    serializer = WindDataSerializer(wind_data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def wind_data_by_max_speed(request, max_speed):
    try:
        max_speed_float = float(max_speed)
        wind_data = WindData.objects.filter(speed__lte=max_speed_float)
        serializer = WindDataSerializer(wind_data, many=True)
        return Response(serializer.data)
    except ValueError:
        return Response({'error': 'Invalid max_speed parameter. Must be a number.'}, status=400)
