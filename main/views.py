import json
import re
#from typing import Union

from django.db.models import Q, QuerySet
from django.http import HttpResponse, JsonResponse, HttpRequest
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import MyUserSerializer
from .models import User

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def connection_test(request: HttpRequest) -> JsonResponse:
    # print(request.headers)
    user = User.objects.get(id=request.user.id)
    serializer = MyUserSerializer(user)
    print(json.dumps(serializer.data))
    return JsonResponse(serializer.data, safe=False)


#@api_view(['GET'])
#@permission_classes([IsAuthenticated])
#def login(request: HttpRequest) -> JsonResponse:
#    user = RidegroupUser.objects.get(id=request.user.id)
#    serializer = MyUserSerializer(user)
#    return JsonResponse(serializer.data, safe=False)
