from django import forms
from .models import Profile


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(label='Image',required=False, error_messages = {'invalid': ("Image files only")}, widget=forms.FileInput)
    class Meta:
        model = Profile
        fields = ['image', 'city', 'birth_date', 'bio']