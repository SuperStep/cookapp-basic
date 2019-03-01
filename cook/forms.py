from django import forms

class IngredentAddForm(forms.Form):
 
    pk = forms.IntegerField()

    def __init__(self, pk=0, *args, **kwargs):
        super(IngredentAddForm, self).__init__(*args, **kwargs)
        self.pk = pk