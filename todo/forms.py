from django import forms
from todo.models import Todo


class TodoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title.....','class':'form-control'}))
    completed = forms.BooleanField(label='Completed',required=False)
    class Meta:
        model = Todo
        fields = '__all__'
