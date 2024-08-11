from django import forms
from .models import Data


class Msg(forms.ModelForm):
    


    class Meta:
        model = Data
        fields='__all__'


        
    name=forms.CharField(max_length=256,required=True,min_length=2,widget=forms.TextInput(attrs={
        "class":"lineform",'placeholder': 'Enter your name','label_class': 'forml',

    }))
    email=forms.CharField(max_length=256,required=True,widget=forms.EmailInput(attrs={
        "class":"lineform",'placeholder': 'Enter your email','label_class': 'forml',

    }))
    text=forms.CharField(max_length=256,required=True,min_length=1,widget=forms.Textarea(attrs={
        "class":"formarea","placeholder": "Enter message",'label_class': 'forml',
    }))    

    # name=forms.CharField()
    # email=forms.EmailField()
    # text=forms.CharField(widget=forms.Textarea)
    # bcat=forms.CharField(required=False,
    #                      widget=forms.HiddenInput,
    #                      validators=[validators.MaxLengthValidator(0)])
    