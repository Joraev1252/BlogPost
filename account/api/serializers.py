from rest_framework import serializers
from account.models import Account


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pk', 'email', 'f_name', 'l_name', 'user_name', 'image', 'age', 'date_birthday', 'phone_number']


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'f_name', 'l_name', 'user_name', 'image', 'age', 'date_birthday', 'phone_number', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            f_name=self.validated_data['f_name'],
            l_name=self.validated_data['l_name'],
            user_name=self.validated_data['user_name'],
            age=self.validated_data['age'],
            phone_number=self.validated_data['phone_number'],

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match!'})
        account.set_password(password)
        account.save()
        return account