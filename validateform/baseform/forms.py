from django import forms

class studentForm(forms.Form):
    Gender ={
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    }
    name = forms.CharField(required=False, error_messages={'required':"Name is Must be Enter"})
    roll = forms.IntegerField( error_messages={'required':"Roll is Must be Enter"})
    pwd1 = forms.CharField(error_messages={'required':"pass1 is Must be Enter"})
    pwd2 = forms.CharField( error_messages={'required':"pass2 is Must be Enter"})
    # gender = forms.CharField(widget=forms.RadioSelect(choices=Gender))
    
    def clean_field(self):
        data = self.cleaned_data["name"]
        if len(data) < 5:
            raise forms.ValidationError("Name shuld be greater than 5 Characters !")
        
        return data
    