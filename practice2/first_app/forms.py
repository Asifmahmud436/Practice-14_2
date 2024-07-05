from django  import forms
from first_app.models import Practice_2

class Practice_2_form(forms.ModelForm):
    class Meta:
        model = Practice_2
        fields = '__all__'