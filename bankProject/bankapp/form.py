from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from django.forms import DateInput

from .models import Data, Branch

Services = (
    ('creditCard', 'Credit Card'),
    ('debitCard', 'Debit Card'),
    ('chequeBook', 'Cheque Book'),)


class DataForm(forms.ModelForm):
    service = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                        choices=Services)
    class Meta:
        widgets = {
            'dob': DateInput(),
        }
        model = Data
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'dist' in self.data:
            try:
                dist_id = int(self.data.get('dist'))
                self.fields['branch'].queryset = Branch.objects.filter(dist_id=dist_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.dist.branch_set.order_by('name')
