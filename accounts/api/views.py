from rest_framework.response import Response
from .serializers import LoginSerializer, RegisterSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework import generics


class LogoutApiView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        """
        Logout class
        """
        logout(request)
        return Response(
            {"non_field_errors": "successfully logged out"},
            status=status.HTTP_200_OK,
        )


class RegisterApiView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        """
        Register class
        """

        serializer = RegisterSerializer(data=request.data, many=False)

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password1"]
            user = User.objects.create_user(
                username=username, password=password
            )
            authenticate(request, username=username, password=password)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        """
        Login view to get user credentials
        """
        serializer = LoginSerializer(data=request.data, many=False)

        if serializer.is_valid():
            user = serializer.validated_data.get("user")
            if user is not None and user.is_active:
                login(request, user)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
