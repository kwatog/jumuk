from rest_framework import serializers

from main.models import *

class MyUserSerializer(serializers.ModelSerializer):
    """
    Serializer for RidegroupUser containing all private user information
    Should only be shown to the user being serialized
    """

    class Meta:
        model = User
        fields = "__all__"

