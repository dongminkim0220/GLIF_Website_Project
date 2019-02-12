class CareerForm(forms.Form):
    career = forms.CharField(label = "", widget = forms.TextInput(attrs = {
        'class': 'form-control',
        'placeholder': 'enter here'
    }))

CareerFormSet = formset_factory(CareerForm)

# form 밑에
career = CareerFormSet()
