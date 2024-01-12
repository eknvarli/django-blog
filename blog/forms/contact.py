from django import forms
from blog.models import ContactModel

class ContactForm(forms.Form): # if you use modelform? you chance forms.Form to forms.ModelForm.
    # ModelForm
    # class Meta:
    #     model = ContactModel
    #     fields = ('email', 'name_surname', 'message')

    email = forms.EmailField(required=True, max_length=100, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter email address'
    }))
    name_surname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Name & Surname'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
    }))