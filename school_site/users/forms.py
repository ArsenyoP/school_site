from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
                "class": "form-control py-4",
                "placeholder": "Введіть ім'я користувача"
            }
        )
    )

    password = forms.CharField(widget=forms.PasswordInput(attrs={
                "class": "form-control py-4",
                "placeholder": "Введіть ім'я користувача"
            }
        )
    )
    class Meta:
        form = User
        fields = ("username", "password")


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введіть ім'я"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введіть прізвище"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введіть ім'я користувача "
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введіть електрону пошту "
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введіть пароль "
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Підтвердіть пароль "
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        "class": "custom-file-label",
        "readonly": True
    }), required=False)


    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2", "image")


class UserProfileForm(UserChangeForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "readonly": True
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control py-4",
        "readonly": True
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        "class": "custom-file-label",
        "readonly": False
    }), required=False)



    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email","image")
