from rest_framework import serializers
from account.models import Account


class  AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pk', 'email', 'f_name', 'l_name', 'user_name', 'image', 'age', 'date_birthday', 'phone_number']


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match!'})
        account.set_password(password)
        account.save()
        return account