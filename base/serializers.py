from django.contrib.auth.models import User
from rest_framework import serializers, validators


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email','first_name')

        extra_kwargs = {
            "email":{
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "This user with that email already exists"

                    )
                ]
            }
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email') 
        first_name = validated_data.get('first_name')


        user= User.objects.create(
            username=username,
            password=password,
            email=email,
            first_name= first_name
        )
            
        return user  

            
