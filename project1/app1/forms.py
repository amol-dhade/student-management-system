from django import forms 
from .models import Student 


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['sid', 'name', 'coll', 'add', 'city', 'state']
        labels = {
            'sid':'STUDENT ID',
            'name':'NAME',
            'coll':'COLLEGE',
            'add':'ADDRESS',
            'city':'CITY',
            'state':'STATE'
        }
        widgets = {
            'sid': forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'coll': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'add': forms.Textarea(
                attrs={
                    'class':'form-control'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'state': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            )
        }
        
