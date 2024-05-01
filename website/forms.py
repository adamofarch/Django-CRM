from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class signUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length="50", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length="50", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(signUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required 8 characters or more, letters, digits, and @/./+/-/_ only. </small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your Password can\'t be similar to your personal information.</li><li>Your password should be atleast 8 character that follows AlphaNumeric pattern.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Please Enter Your Password Again for Verification. </small></span>'


class addRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), label="")
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}), label="")
    zip_code = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}), label="")

    class Meta:
        model = Record
        exclude = ('user', )