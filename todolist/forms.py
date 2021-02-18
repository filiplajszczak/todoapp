from django import forms
class Todolistform(forms.Form):
    text=forms.CharField(max_length=45,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'Enter todo e.g. grocery shopping','aria-label':'Todo','aria-describedby':'add-btn'}))
