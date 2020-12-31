from .models import Teams,TeamScoring
from django import forms


class Teams_Form(forms.ModelForm):
    class Meta:
        model = Teams
        fields = ['name']

class Update_Team_Form(forms.ModelForm):
    class Meta:
        model = TeamScoring
        fields = ['options']

    def __init__(self, *args, **kwargs):
        self.Teams = kwargs.pop('Teams')
        super(Update_Team_Form, self).__init__(*args, **kwargs)
    
    def save(self, commit=True):
        inst = super(Update_Team_Form, self).save(commit=False)
        inst.Teams = self.Teams
        if commit:
            inst.save()
            #self.save_m2m()
        return inst