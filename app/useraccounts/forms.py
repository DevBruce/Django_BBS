from django import forms
from django.contrib.auth import get_user_model

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
        label='Password Confirm',
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
            raise forms.ValidationError('Password and Password Confirm field values are not equal')
        return password_confirm

    def save(self):
        if self.errors:
            raise ValueError('Validation Failed')
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        return user
