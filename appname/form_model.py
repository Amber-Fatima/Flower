from django import forms
from .models import Item


# https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/
# helper form class to create forms with the content fiels of an already existing data to update or add more objects to it
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "item_desc", "price", "image"]
