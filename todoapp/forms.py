from django import forms
from todoapp.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'date']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        # }