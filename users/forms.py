from random import choices

from .models import Profile
from django import forms


class UserForm(forms.ModelForm):
    class Meta:

        model = Profile
        fields = ["is_approved", ]

        widgets = {
            "is_approved": forms.RadioSelect(choices=[(True, "APPROVED"), (False, "NOT APPROVED")]),
        }

