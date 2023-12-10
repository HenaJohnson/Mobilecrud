from django import forms
from features.models import Mobilemodel

class Mobileform(forms.ModelForm):

    # brand = forms.CharField()
    # modls= forms.CharField()
    # color = forms.CharField()
    # price = forms.IntegerField()
    # year = forms.IntegerField()  

    class Meta:
        model=Mobilemodel
        fields='__all__'

