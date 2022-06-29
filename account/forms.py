from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from account.models import Account


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address")

    class Meta:
        model = Account
        fields = ['email', 'password1', 'password2']


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['email', 'password']

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid inputs")


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'f_name',
            'l_name',
            'user_name',
            'image',
            'age',
            'date_birthday',
            'phone_number',
        ]
        enctype = "multipart/form-data"

class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'user_name',)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email is already in use.' % account)



    def clean_username(self):
        if self.is_valid():
            user_name = self.cleaned_data['user_name']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(user_name=user_name)
            except Account.DoesNotExist:
                return user_name
            raise forms.ValidationError('Username "%s" is already in use.' % user_name)
