from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username    = serializers.CharField()
    password    = serializers.CharField()

    def validate(self, data):
        username= data.get("username")
        password= data.get("password")
        print(username)
        print(password)
        user = authenticate(username=username, password= password )
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model           = User
        fields          = ('id', 'name', 'email', 'username', 'password')
        extra_Kwargs    = {'password':{'write_only': True}}

        def create(self, validated_data):
            user        = User(
                        name        = validated_data["name"],
                        username    = validated_data["username"],
                        email       = validated_data["email"],
                        # password    = validated_data["password"]
            )
            password    = validated_data["password"]
            user.set_password(password)
            user.save()
            return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model   = User
        fields  = ('id', 'name', 'email', 'username')