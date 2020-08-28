from django import forms
from TownSquare.models import MyUser, Ticket


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

class Ticket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description"]

class MyUser(forms.Form):
    name = forms.CharField(max_length=80)
    bio = forms.CharField(widget=forms.Textarea)