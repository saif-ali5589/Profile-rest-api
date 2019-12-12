from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_app import serializer

class HelloApiViews(APIView):
    """Test api View"""

    serializer_class = serializer.HelloSerializer

    def get(self,request,format=None):
        """Return a list of api views"""
        an_apiview = [
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'Is similar to a tradional Django View',
            'Gives you most control over  your appilication logic',
            'Is mapped manually to URLs',
            ]

        return Response({'Message':'Helllo!','an_apiview':an_apiview})

    def post(self,request):
        """create hello message with our name"""
        """serializer also used for to validate data"""
        #to validate a serialier call is_validate function
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            #message = f'Saif{name}'
            message = f'my name is khan'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """handle update an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """handle parttial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
