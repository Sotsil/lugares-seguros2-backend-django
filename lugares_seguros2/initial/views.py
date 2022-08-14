from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework import status
#from places.models import Place
#from places.models import PlaceSerializer
 


class HelloDrF(APIView):
    def get(self, request, format=None):
        return Response({"message": "Hello World from DRF!!"}) #aqui se devuelve un json


    