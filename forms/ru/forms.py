from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.localflavor.ru.forms import RUPostalCodeField

from postal.forms import PostalAddressForm


class RUPostalAddressForm(PostalAddressForm):
    line1 = forms.CharField(label=_(u"Street"), max_length=100)
    city = forms.CharField(label=_(u"City"), max_length=100)
    code = RUPostalCodeField(label=_(u"Zip Code"))

    def __init__(self, *args, **kwargs):
        super(RUPostalAddressForm, self).__init__(*args, **kwargs)
        self.fields.pop('line2')
        self.fields.pop('state')
        self.fields['country'].initial = "RU"
