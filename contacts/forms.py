from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(label="Name", max_length=200, widget=forms.TextInput(attrs={'placeholder':'Company Name'}))
  email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'placeholder':'Company Email'}))
  phone_number = forms.CharField(label="Phone Number", max_length=11)
  services_needed = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'What services do you want?'}))