from django.contrib import admin
from .forms import AgentAdminForm
from .models import *


# Admin setup for State and District
@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state')
    list_filter = ('state',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Taluka)
class TalukaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state', 'district')
    list_filter = ('state', 'district')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state', 'district', 'taluka')
    list_filter = ('state', 'district', 'taluka')
    search_fields = ('name',)
    ordering = ('name',)


# Admin for Location-based models

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('id', 'bank_name', 'state', 'district', 'contact_number')
    list_filter = ('state', 'district')
    search_fields = ('bank_name', 'contact_number')
    ordering = ('bank_name',)
    autocomplete_fields = ['state', 'district']


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    form = AgentAdminForm
    list_display = ('id', 'agent_name', 'state', 'district', 'contact_number')
    list_filter = ('state', 'district')
    search_fields = ('agent_name', 'contact_number')
    ordering = ('agent_name',)
    autocomplete_fields = ['state', 'district']


@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'state', 'district', 'contact_number')
    list_filter = ('state', 'district')
    search_fields = ('full_name', 'contact_number')
    ordering = ('full_name',)
    autocomplete_fields = ['state', 'district']


@admin.register(AgentAssignedToBank)
class AgentAssignedToBankAdmin(admin.ModelAdmin):
    list_display = ('id', 'bank', 'agent', 'state', 'district')
    list_filter = ('state', 'district', 'bank')
    search_fields = ('agent__agent_name', 'bank__bank_name')
    ordering = ('bank', 'agent')
    autocomplete_fields = ['state', 'district', 'bank', 'agent']


@admin.register(UserAssignedToBank)
class UserAssignedToBankAdmin(admin.ModelAdmin):
    list_display = ('id', 'bank', 'user', 'state', 'district')
    list_filter = ('state', 'district', 'bank')
    search_fields = ('user__full_name', 'bank__bank_name')
    ordering = ('bank', 'user')
    autocomplete_fields = ['state', 'district', 'bank', 'user']


@admin.register(UserPaymentStatement)
class UserPaymentStatementAdmin(admin.ModelAdmin):
    list_display = ('id', 'bank', 'user', 'amount_type', 'state', 'district')
    list_filter = ('state', 'district', 'bank', 'amount_type')
    search_fields = ('user__full_name', 'bank__bank_name', 'amount_type')
    ordering = ('user', 'bank')
    autocomplete_fields = ['state', 'district', 'bank', 'user']


@admin.register(UserLoanAddStatement)
class UserLoanAddStatementAdmin(admin.ModelAdmin):
    list_display = ('id', 'bank', 'user', 'loan_amount', 'state', 'district')
    list_filter = ('state', 'district', 'bank')
    search_fields = ('user__full_name', 'bank__bank_name')
    ordering = ('user',)
    autocomplete_fields = ['state', 'district', 'bank', 'user']


@admin.register(UserLoanStatement)
class UserLoanStatementAdmin(admin.ModelAdmin):
    list_display = ('id', 'bank', 'user', 'loan_amount', 'state', 'district')
    list_filter = ('state', 'district', 'bank')
    search_fields = ('user__full_name', 'bank__bank_name')
    ordering = ('user',)
    autocomplete_fields = ['state', 'district', 'bank', 'user']


@admin.register(BankPrivacyPolicy)
class BankPrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('id', 'bank', 'state', 'district')
    list_filter = ('state', 'district', 'bank')
    ordering = ('bank',)
    autocomplete_fields = ['state', 'district', 'bank']


@admin.register(BankAbout)
class BankAboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'bank', 'state', 'district')
    list_filter = ('state', 'district', 'bank')
    ordering = ('bank',)
    autocomplete_fields = ['state', 'district', 'bank']
