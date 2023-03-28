from .models import Product, Branch_one,  Branch_two, Branch_three, Central_product
from django import forms




class NewDeliForm(forms.ModelForm):
    class Meta:
        model = Branch_one
        fields = ('name', 'weight', 'stock')
        
        
        
        
class MoreDeliForm(forms.ModelForm):
    OPTIONS = (
        ('Branch_one', 'Branch_one'),
        ('Branch_two', 'Branch_two'),
        ('Branch_three', 'Branch_three'),
        ('Central_product', 'Central_product')
    )
    choice = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect())

    class Meta:
        model = Product
        fields = ('name', 'weight', 'stock')
        

class HTML5DateInput(forms.DateInput):
    input_type = 'date'



class MyForm(forms.Form):
    start_date = forms.DateField(widget=HTML5DateInput)
    end_date = forms.DateField(widget=HTML5DateInput)