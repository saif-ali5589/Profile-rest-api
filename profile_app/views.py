from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiViews(APIView):
    """Test api View"""

    def get(self,request,format=None):
        """Return a list of api views"""
        an_apiview = [
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'Is similar to a tradional Django View',
            'Gives you most control over  your appilication logic',
            'Is mapped manually to URLs',
            ]

        return Response({'Message':'Helllo!','an_apiview':an_apiview})
