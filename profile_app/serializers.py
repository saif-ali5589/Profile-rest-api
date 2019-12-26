from rest_framework import serializers
from profile_app import models

class HelloSerializer(serializers.ModelSerializer):
    """serializes a name field for test our APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer a user profileuser"""
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        #tuple of object that can accessible through an api
        #we have make password field to write only not accessible to anyone
        extra_kwargs = {'password':
        {
        'write_only':True,
        'style':
        {
        'input_type':'password'}
        }
        }

    def create(self,validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
        email=validated_data['email'],
        name=validated_data['name'],
        password=validated_data['password']
        )

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
