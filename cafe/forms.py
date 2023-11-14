from django import forms
from . models import Reservation, Employees, Offers

class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'

class OffersForm(forms.ModelForm):
    class Meta:
        model = Offers
        fields = '__all__'

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)