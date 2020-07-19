from django import forms 

class Uploadform(forms.Form):
    animal = forms.CharField(max_length=100)
    img_file = forms.ImageField()
