from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profile_app import serializers
from profile_app import models
from rest_framework.authentication import TokenAuthentication
from profile_app import permissions
from rest_framework import filters

class HelloApiViews(APIView):
    """Test api View"""

    serializer_class = serializers.HelloSerializer

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
            message = f'name'
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


class HelloViewSet(viewsets.ViewSet):
    """Test api viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a heelo message"""


    def create(self,request):
        """create data"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Saif{name}'
            #message = f'my name is khan'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retreive(self,request,pk=None):
        """get request"""
        return Response({'method':'GET'})

    def update(self,request,pk=None):
        """put"""
        return Response({'method':'PUT'})

    def partial_update(self,request,pk=None):
        """PATCH"""
        return Response({'method':'PATCH'})

    def destroy(self,request,pk=None):
        """delete"""
        return Response({'method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    """Handle creating, creating and updating profiles"""
    ...
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
