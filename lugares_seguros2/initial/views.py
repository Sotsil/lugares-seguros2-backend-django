from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloDrF(APIView):
    def get(self, request, format=None):
        return Response({"message": "Hello World from DRF!!"}) #aqui se devuelve un json


    
