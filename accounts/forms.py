from django import forms
from .models import OtherUser
from django.contrib.auth.forms import UserCreationForm,UserChangeForm



class CreatedUser(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = OtherUser
        fields =UserCreationForm.Meta.fields

class ChangeUser(UserChangeForm):
    class Meta:
        model = OtherUser
        fields = UserChangeForm.Meta.fields
