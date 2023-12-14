from .models import Product
from django.forms import ModelForm, TextInput, NumberInput, ImageField
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'size', 'quantity',]

        widgets={
            "name": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Наименование товара'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость'
            }),
            "size": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Размер изделия'
            }),
            "quantity": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество на складе'
            }),
        }
