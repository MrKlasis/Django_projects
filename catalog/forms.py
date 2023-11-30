from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'img', 'category', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fild in self.fields.items():
            fild.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        ban_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in ban_words:
            if word in cleaned_data:
                raise forms.ValidationError('Используются запретные слова')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        ban_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in ban_words:
            if word in cleaned_data:
                raise forms.ValidationError('Используются запретные слова')
        return cleaned_data


class ModeratorProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'category')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, fild in self.fields.items():
                fild.widget.attrs['class'] = 'form-control'


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        # exclude = ('activate',)
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fild in self.fields.items():
            if field_name != 'activate':
                fild.widget.attrs['class'] = 'form-control'
