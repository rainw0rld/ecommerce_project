from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny

from users.models import Customer
from users.serializers import CustomerSerializer


class CustomerAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        serializer = CustomerSerializer(data=request.user, fields=('email', 'first_name', 'last_name'))
        return Response(serializer.data, status=True)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
