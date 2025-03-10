from django import forms
from .models import Tour, Review


class TourForm(forms.ModelForm):

    HOME_PAGE_CHOICES = [("Yes", "Yes"), ("No", "No")]

    home_page = forms.ChoiceField(
        choices=HOME_PAGE_CHOICES,
        widget=forms.RadioSelect(attrs={"class": "home_page-radio"}),
    )

    CATEGORY_CHOICES = [

        ("Safaris", "Safaris"),
        ("Beach Tours", "Beach Tours"),
        ("City Tours", "City Tours"), ("Cultural Tours", "Cultural Tours"),
        ("Transfers", "Transfers"),
    ]

    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.RadioSelect(attrs={"class": "category-radio"}),
    )

    SUBCATEGORY_COICHES = [

        ("Maputo National Park", "Maputo National Park"), ("Kruger National Park", "Kruger National Park"), ("eSwatini Full day Tour", "eSwatini Full day Tour"),
        ("Inhaca Island", "Inhaca Island"), ("Macaneta Full day Trip", "Macaneta Full day Trip"),("Ponta d'ouro Full day Tour", "Ponta d'ouro Full day Tour"),
        ("Walking Tours", "Walking Tours"), ("On wheels Tours", "On Wheels Tours"),
        ("eSwatini Culture", "eSwatini Culture"), ("maputo Culture", "maputo Culture"),("Other Tours","Other Tours"),
        ("Cultural Tours", "Cultural Tours"), ("Other Transfers", "Other Transfers"),("Airport & Port transfers", "Airport & Port Transfers"),
    ]

    subcategory = forms.ChoiceField(
        choices=SUBCATEGORY_COICHES, widget=forms.RadioSelect(attrs={"class": "subcategory-radio"}),
    )

    class Meta:

        model = Tour
        fields = ["title", "home_page", "short_description", "full_description", "category", "subcategory", "image", "image_2", "image_3",
                  "price", "duration", "participants_ages", "pick_up_location", "language", "start_time", "included", "expected",
                  "accessibility", "additional_info", "cancellation_policy", "FAQ", ]


class ReviewForm(forms.ModelForm):

   class Meta:

       # Include Field Tour
       model = Review
       fields = ["title", "text", "reviewer_name", "reviewer_image",]

