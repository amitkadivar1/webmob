from django import forms
class InsertNewProduct(forms.Form):
    name=forms.CharField()
    price=forms.IntegerField()
    description=forms.CharField(widget=forms.Textarea())
    quantity=forms.IntegerField()
