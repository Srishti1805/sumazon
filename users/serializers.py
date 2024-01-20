from .models import Users
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username','email','id','address','number','profilePicture','password']
    
    def create(self, validated_data):
        # print("I am authenticated", validated_data, flush=True)
        user = Users.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

        