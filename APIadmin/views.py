from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import UserSerializer, LimitedUserSerializer
from django.contrib.auth.models import User

@api_view(['POST'])
def Login(request):

    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({'error': 'Invalid Credentials'}, status = status.HTTP_400_BAD_REQUEST)

    token = Token.objects.get(user=user)
    user_serializer = LimitedUserSerializer(user)

    return Response({'token' : token.key, 'user' : user_serializer.data }, status = status.HTTP_200_OK)

@api_view(['POST'])
def Register(request):

    user_serializer = UserSerializer(data = request.data)

    if user_serializer.is_valid():

        user_serializer.save()
        
        user = User.objects.get(username=user_serializer.data['username'])
        user.set_password(user_serializer.data['password'])
        user.save()

        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key, 'user': user_serializer.data},status = status.HTTP_201_CREATED)

    return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Logout(request):
    try:
        token = request.auth
        if token:
            token.delete()
            return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No token provided'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': 'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)