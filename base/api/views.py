from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import JsonResponse
from base.models import Room
from .serializers import RoomSerializer

@api_view(['Get'])
def getRoutes(request):
    routes = [
        'Get /api',
        'Get /api/rooms',
        'Get /api/rooms/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializers = RoomSerializer(rooms, many=True)
    return Response(serializers.data) 

@api_view(['GET'])
def getRoom(request, pk):
    rooms = Room.objects.get(id=pk)
    serializers = RoomSerializer(rooms, many=False)
    return Response(serializers.data) 