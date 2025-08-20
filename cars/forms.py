from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


    #para validar o campo de valor
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'O valor deve ser maior que 20.000')
        return value

    #para validar o campo de ano do modelo
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'O ano de fabricação deve ser igual ou maior que 1975')
        return factory_year
    