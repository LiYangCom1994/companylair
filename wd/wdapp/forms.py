from django import forms

from django.contrib.auth.models import User
from wdapp.models import Company, Cargo, Business, BusinessOrder, Stop,DriverExpense,Trip,Driver

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    username=  forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ("username", "password")


class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ("email",)

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['company_id','user']
        #fields = '__all__'("name", "phone", "address", )#"logo")
class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = ['company_id','user','driver_id']
        #fields = '__all__'("name", "phone", "address", )#"logo")
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['business_id','user']

class DriverExpenseForm(forms.ModelForm):
    class Meta:
        model = Cargo
        exclude = ['expense_id']
       # fields = '__all__'("company",)


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        exclude = ['cargo_id']

class StopForm(forms.ModelForm):
    class Meta:
        model = Stop



        exclude = ['stop_id']
class BusinessOrderForm(forms.ModelForm):
    class Meta:
        model = BusinessOrder

        exclude = ['business_id','order_id','weight','volume','date_created']




class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        exclude = ['trip_id']


