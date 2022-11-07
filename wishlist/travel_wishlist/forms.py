from django import forms
from models import Place


class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')

class DateInput(forms.DateInput):  
    input_type = 'date'

class TripReviewForm(forms.ModelForm):
    class Meta:  #describes information about the object
        model = Place
        fields = ('notes', 'date_visited', 'photo') #strings 
        widgets = {
            'date_visited': DateInput()
        }
