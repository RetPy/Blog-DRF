from apps.users.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ('id', 'username', 'age', 'gender', 'password')

    def create(self, validated_data):

        user = super().create(validated_data)
        password = validated_data['password']
        user.set_password(password)
        user.save()
        return user
