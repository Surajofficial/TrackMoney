from django import forms
from django_select2.forms import Select2Widget
from django_select2.forms import ModelSelect2Widget
from .models import (
    Bank, Agent, UserDetail, AgentAssignedToBank, UserAssignedToBank,
    UserPaymentStatement, UserLoanAddStatement, UserLoanStatement,
    BankPrivacyPolicy, BankAbout, State, District
)


class StateWidget(ModelSelect2Widget):
    model = State
    search_fields = ['name__icontains']  # Enables searching within state names


class DistrictWidget(ModelSelect2Widget):
    model = District
    # Enables searching within district names
    search_fields = ['name__icontains']
    # Filters districts based on the selected state
    dependent_fields = {'state': 'state'}


class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'
        widgets = {
            'state': StateWidget,
            'district': DistrictWidget,
        }


class AgentAdminForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'
        widgets = {
            # Use your actual URL for state
            'state': Select2Widget,
            'district': Select2Widget,
        }




class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = '__all__'
        widgets = {
            'state': StateWidget,
            'district': DistrictWidget,
        }


class AgentAssignedToBankForm(forms.ModelForm):
    class Meta:
        model = AgentAssignedToBank
        fields = '__all__'
        widgets = {
            'state': StateWidget,
            'district': DistrictWidget,
            'bank': ModelSelect2Widget(model=Bank, search_fields=['bank_name__icontains']),
            'agent': ModelSelect2Widget(model=Agent, search_fields=['agent_name__icontains']),
        }


class UserAssignedToBankForm(forms.ModelForm):
    class Meta:
        model = UserAssignedToBank
        fields = '__all__'
        widgets = {
            'state': StateWidget,
            'district': DistrictWidget,
            'bank': ModelSelect2Widget(model=Bank, search_fields=['bank_name__icontains']),
            'user': ModelSelect2Widget(model=UserDetail, search_fields=['full_name__icontains']),
        }


class UserPaymentStatementForm(forms.ModelForm):
    class Meta:
        model = UserPaymentStatement
        fields = '__all__'
        widgets = {
            'state': StateWidget,
            'district': DistrictWidget,
            'bank': ModelSelect2Widget(model=Bank, search_fields=['bank_name__icontains']),
            'user': ModelSelect2Widget(model=UserDetail, search_fields=['full_name__icontains']),
            'agent': ModelSelect2Widget(model=Agent, search_fields=['agent_name__icontains']),
        }


class UserLoanAddStatementForm(forms.ModelForm):
    class Meta:
        model = UserLoanAddStatement
        fields = '__all__'
        widgets = {
            'state': StateWidget,
            'district': DistrictWidget,
            'bank': ModelSelect2Widget(model=Bank, search_fields=['bank_name__icontains']),
            'user': ModelSelect2Widget(model=UserDetail, search_fields=['full_name__icontains']),
        }


class UserLoanStatementForm(forms.ModelForm):
    class Meta:
        model = UserLoanStatement
        fields = '__all__'
        widgets = {
            'state': StateWidget,
            'district': DistrictWidget,
            'bank': ModelSelect2Widget(model=Bank, search_fields=['bank_name__icontains']),
            'user': ModelSelect2Widget(model=UserDetail, search_fields=['full_name__icontains']),
        }


class BankPrivacyPolicyForm(forms.ModelForm):
    class Meta:
        model = BankPrivacyPolicy
        fields = '__all__'
        widgets = {
            'state': StateWidget,
            'district': DistrictWidget,
            'bank': ModelSelect2Widget(model=Bank, search_fields=['bank_name__icontains']),
        }


class BankAboutForm(forms.ModelForm):
    class Meta:
        model = BankAbout
        fields = '__all__'
        widgets = {
            'state': StateWidget,
            'district': DistrictWidget,
            'bank': ModelSelect2Widget(model=Bank, search_fields=['bank_name__icontains']),
        }
