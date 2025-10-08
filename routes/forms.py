from django import forms
from .models import Route

# This form is used to add/edit Route entries in the database
class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['from_airport', 'to_airport', 'position', 'duration']  # Fields to include in the form


class NodeSearchForm(forms.Form):
    from_airport = forms.CharField()
    direction = forms.ChoiceField(choices=[('left', 'Left'), ('right', 'Right')])
    n = forms.IntegerField(min_value=1)

