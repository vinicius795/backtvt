from django.contrib.auth.models import User

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only = True, required=False)

    def create(self, validated_data):
        
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        user = instance
        password = validated_data.pop("password")
        user.set_password(password)
        user.save()
        return super(UserSerializer, self.update(instance, validated_data))

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'first_name', 'last_name', 'password', 'is_staff', 'profile']