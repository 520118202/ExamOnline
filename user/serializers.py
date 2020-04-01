from django.contrib.auth.models import User
from rest_framework import serializers

from user.models import Student


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    # 覆盖外键字段
    #user = UserDetailSerializer()

    class Meta:
        model = Student
        fields = '__all__'
