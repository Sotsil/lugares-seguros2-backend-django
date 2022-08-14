from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from places.models import Place
from places.serializers import PlaceSerializer



class PlaceView(APIView):

    parser_classes = (MultiPartParser, FormParser)


    def get(self, request):
        places = Place.objects.all()
        print(places)
        serializer = PlaceSerializer(places, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK )

    def post(self, request):
        print(request.data)
        try:
            file = request.data['image']
            request.data['image'] = file
        except KeyError:
            file = None
    
        serializer = PlaceSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

class PlaceSingleView(APIView):
    def put(self, request, id):
        place = Place.objects.get(id = id)
        serializer = PlaceSerializer(place, data = request.data, partial= True)  #aqui se indica q puede hacer modif parciales
        serializer.is_valid(raise_exception=True)
        serializer.save()  #AQUI SE GUARDA EN LA BD
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        place = Place.objects.get(id = id)
        place.delete()
        return Response({"message":"lugar eliminado correcamente"}, status=status.HTTP_204_NO_CONTENT)



# Create your views here.
