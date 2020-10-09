from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        if (User.objects.filter(username=username).exists()):
            raise serializers.ValidationError(
                {"username": "User name addresses must be unique."})
        user = User(username=username)
        user.set_password(password)
        user.save()
        return user