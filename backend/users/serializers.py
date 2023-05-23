from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    role = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    surname = serializers.CharField()
    phone = serializers.CharField()


class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    surname = serializers.CharField()
    phone = serializers.CharField()


class UserUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(required=False, allow_null=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    surname = serializers.CharField()
    phone = serializers.CharField()


class UserInfoSerializer(serializers.Serializer):
    birthdate = serializers.DateField()
    university_name = serializers.CharField()
    university_year = serializers.IntegerField()
    job_experience = serializers.CharField()
    skills = serializers.CharField()
    departments = serializers.CharField()
