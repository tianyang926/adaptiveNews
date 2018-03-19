from rest_framework import serializers
from users.models import User, LANGUAGE_CHOICES, STYLE_CHOICES


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'age', 'gender', 'created_date')
    # id = serializers.IntegerField(read_only=True)
    # username = serializers.CharField(required=True, max_length=100)
    # password = serializers.CharField(required=True)

    # # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # # linenos = serializers.BooleanField(required=False)
    # age = serializers.IntegerField(required=True)
    # gender = serializers.CharField(required=True, max_length=100)
    # created_date = serializers.CharField(required=True)


    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return User.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Users` instance, given the validated data.
    #     """
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.password = validated_data.get('password', instance.code)
    #     instance.age = validated_data.get('age', instance.age)
    #     instance.gender = validated_data.get('gender', instance.gender)
    #     instance.created_date = validated_data.get('created_date', instance.created_date)
    #     instance.save()
    #     return instance