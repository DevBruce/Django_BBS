from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class SignUpForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label='UserName',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Password Confirmation',
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            self.fields['username'].widget.attrs['class'] += ' is-invalid'
            raise forms.ValidationError('Username already exists')
        return username

    def clean_password_confirm(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if not password == password_confirm:
            self.fields['password'].widget.attrs['class'] += ' is-invalid'
            self.fields['password_confirm'].widget.attrs['class'] += ' is-invalid'
            raise forms.ValidationError('Password and Password Confirmation field values are not equal')
        return password_confirm

    def save(self):
        if self.errors:
            raise ValueError('Validation Failed')
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        return user


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._user = None

    @property
    def user(self):
        if self.errors:
            raise ValueError('Validation Failed')
        return self._user

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autofocus': True,
            }
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            self.fields['username'].widget.attrs['class'] += ' is-invalid'
            self.fields['password'].widget.attrs['class'] += ' is-invalid'
            raise forms.ValidationError('Invalid UserName or Password')
        self._user = user
