from django.forms import ModelForm
from .models import Cards


class Create_Card_Form(ModelForm):
    class Meta:
        model = Cards
        fields = ['card_title', 'description', 'image','realtor' ]
