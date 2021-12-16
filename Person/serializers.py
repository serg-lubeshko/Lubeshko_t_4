from rest_framework import serializers

from Person.models import MyUser


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = MyUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = MyUser
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", "status" )