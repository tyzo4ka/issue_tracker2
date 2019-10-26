from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label="Username", required=True)
    password = forms.CharField(max_length=100, label="Password", required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, label="Confirm Password", required=True,
                                       widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError("User with this username already exists", code="username_exists")

        except User.DoesNotExist:
            return username

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data['password']
        password_2 = self.cleaned_data["password_confirm"]
        data = self.cleaned_data
        if not data.get('first_name') and not data.get('last_name'):
            raise ValidationError("One of the following fields: first_name, last_name should be filled",
                                  code='first_name_last_name_criteria_empty')
        if password_1 != password_2:
            raise ValidationError("Passwords does not match", code="passwords_does_not_match")
        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('User with this email already exists', code='user_email_exists')
        except User.DoesNotExist:
            return email

    class Meta:
        model = User
        fields = ['username', 'password', "password_confirm", 'first_name', 'last_name', 'email']
