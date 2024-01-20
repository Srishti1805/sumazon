# libraries imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.serializers import ValidationError
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from .models import Users
from .serializers import RegisterSerializer
from rest_framework.views import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken



# Register Users
class RegisterUserView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = RegisterSerializer(data = data)
            email = request.data.get('email', None)
            # user = Users.objects.get(email=email)
            # if user.isVerified:
            #     return Response("User already register", status=status.HTTP_400_BAD_REQUEST)
            # else:
            #     user.delete()
            # userInput = request.data
            # userInput['otp'] = str(random.randint(100000, 999999))
            # userInput["signInMethod"] = "email"
            # serializer = RegisterSerializer(data=userInput)

            if serializer.is_valid():
                serializer.save()  # user is saved in db
                return Response("ok", status.HTTP_201_CREATED)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

       
        except:
            Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)






# Logout View
class LogoutView(APIView):
    def post(self, request):
        try:
            if "refresh" not in request.data:
                return Response({"detail": "refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

            # Black list token
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)