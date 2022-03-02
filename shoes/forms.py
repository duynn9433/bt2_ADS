from django import forms

from clothes.models import Cloth, Vendor
from shoes.models import Shoe, Brand


class CustomMCF(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name + ", " + obj.country


class AddShoe(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ['name', 'price', 'color', 'size', 'brand']

    brand = CustomMCF(
        queryset=Brand.objects.all()
    )


class AddBrand(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'country']
