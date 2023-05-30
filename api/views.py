from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from item.models import Item
from .serializers import ItemSerializer

# Create your views here.

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)