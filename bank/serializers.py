from rest_framework import serializers
from .models import *

# State and District serializers to use as nested serializers


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name']


class DistrictSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = District
        fields = ['id', 'name', 'state']


class TalukaSerializer(serializers.ModelSerializer):
    state_id = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(), source='state')
    district_id = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all(), source='district')
    state = StateSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)

    class Meta:
        model = Taluka
        fields = ['id', 'name', 'state_id', 'district_id', 'state', 'district']


class VillageSerializer(serializers.ModelSerializer):
    state_id = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(), source='state')
    district_id = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all(), source='district')
    taluka_id = serializers.PrimaryKeyRelatedField(
        queryset=Taluka.objects.all(), source='taluka')
    state = StateSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    taluka = TalukaSerializer(read_only=True)

    class Meta:
        model = Village
        fields = ['id', 'name', 'state_id', 'district_id',
                  'taluka_id', 'state', 'district', 'taluka']

# Bank Serializer with dynamic fields for fetching data


class BankLoginSerializer(serializers.Serializer):
    contact_number = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=6)


class AgentLoginSerializer(serializers.Serializer):
    contact_number = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=6)


class UserDetailLoginSerializer(serializers.Serializer):
    contact_number = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=6)


class BankSerializer(serializers.ModelSerializer):
    state_id = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(), source='state')
    district_id = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all(), source='district')
    taluka_id = serializers.PrimaryKeyRelatedField(
        queryset=Taluka.objects.all(), source='taluka')
    village_id = serializers.PrimaryKeyRelatedField(
        queryset=Village.objects.all(), source='village')

    state = serializers.SerializerMethodField()
    district = serializers.SerializerMethodField()
    taluka = serializers.SerializerMethodField()
    village = serializers.SerializerMethodField()

    class Meta:
        model = Bank
        fields = '__all__'

    def get_state(self, obj):
        return obj.state.name if obj.state else None

    def get_district(self, obj):
        return obj.district.name if obj.district else None

    def get_taluka(self, obj):
        return obj.taluka.name if obj.taluka else None

    def get_village(self, obj):
        return obj.village.name if obj.village else None

# Agent Serializer


# Mixin for location-related fields and methods
class BaseLocationSerializerMixin:
    def get_state(self, obj):
        return obj.state.name if obj.state else None

    def get_district(self, obj):
        return obj.district.name if obj.district else None

    def get_taluka(self, obj):
        return obj.taluka.name if obj.taluka else None

    def get_village(self, obj):
        return obj.village.name if obj.village else None


# Agent Serializer
class AgentSerializer(serializers.ModelSerializer, BaseLocationSerializerMixin):
    state_id = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(), source='state')
    district_id = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all(), source='district')
    taluka_id = serializers.PrimaryKeyRelatedField(
        queryset=Taluka.objects.all(), source='taluka')
    village_id = serializers.PrimaryKeyRelatedField(
        queryset=Village.objects.all(), source='village')

    state = serializers.SerializerMethodField()
    district = serializers.SerializerMethodField()
    taluka = serializers.SerializerMethodField()
    village = serializers.SerializerMethodField()

    class Meta:
        model = Agent
        fields = [
            'id', 'agent_name', 'state_id', 'district_id', 'taluka_id', 'village_id',
            'state', 'district', 'taluka', 'village', 'address', 'contact_number',
            'uid_number', 'birth_date', 'photo', 'uid_doc'
        ]


# UserDetail Serializer
class UserDetailSerializer(serializers.ModelSerializer, BaseLocationSerializerMixin):
    state_id = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(), source='state')
    district_id = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all(), source='district')
    taluka_id = serializers.PrimaryKeyRelatedField(
        queryset=Taluka.objects.all(), source='taluka')
    village_id = serializers.PrimaryKeyRelatedField(
        queryset=Village.objects.all(), source='village')

    state = serializers.SerializerMethodField()
    district = serializers.SerializerMethodField()
    taluka = serializers.SerializerMethodField()
    village = serializers.SerializerMethodField()

    class Meta:
        model = UserDetail
        fields = '__all__'


# AgentAssignedToBank Serializer
class AgentAssignedToBankSerializer(serializers.ModelSerializer, BaseLocationSerializerMixin):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())
    agent = serializers.PrimaryKeyRelatedField(queryset=Agent.objects.all())
    state_id = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(), source='state')
    district_id = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all(), source='district')
    taluka_id = serializers.PrimaryKeyRelatedField(
        queryset=Taluka.objects.all(), source='taluka')
    village_id = serializers.PrimaryKeyRelatedField(
        queryset=Village.objects.all(), source='village')

    bank_name = serializers.SerializerMethodField()
    agent_name = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    district = serializers.SerializerMethodField()
    taluka = serializers.SerializerMethodField()
    village = serializers.SerializerMethodField()

    class Meta:
        model = AgentAssignedToBank
        fields = '__all__'

    def get_bank_name(self, obj):
        return obj.bank.bank_name if obj.bank else None

    def get_agent_name(self, obj):
        return obj.agent.agent_name if obj.agent else None


# UserAssignedToBank Serializer
class UserAssignedToBankSerializer(serializers.ModelSerializer, BaseLocationSerializerMixin):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())
    user = serializers.PrimaryKeyRelatedField(
        queryset=UserDetail.objects.all())

    state_id = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(), source='state')
    district_id = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all(), source='district')
    taluka_id = serializers.PrimaryKeyRelatedField(
        queryset=Taluka.objects.all(), source='taluka')
    village_id = serializers.PrimaryKeyRelatedField(
        queryset=Village.objects.all(), source='village')

    bank_name = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    district = serializers.SerializerMethodField()
    taluka = serializers.SerializerMethodField()
    village = serializers.SerializerMethodField()

    class Meta:
        model = UserAssignedToBank
        fields = '__all__'

    def get_bank_name(self, obj):
        return obj.bank.bank_name if obj.bank else None

    def get_user_name(self, obj):
        return obj.user.full_name if obj.user else None

# UserPaymentStatement Serializer


class UserPaymentStatementSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField for relational data
    bank_id = serializers.PrimaryKeyRelatedField(
        queryset=Bank.objects.all(), source='bank')
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=UserDetail.objects.all(), source='user')
    agent_id = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.all(), source='agent', allow_null=True, required=False
    )

    # Additional fields to fetch related data
    bank_name = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    agent_name = serializers.SerializerMethodField()

    class Meta:
        model = UserPaymentStatement
        fields = [
            'id', 'bank_id', 'user_id', 'agent_id', 'bank_name',
            'user_name', 'agent_name', 'amount_type', 'yesterday_total_amount',
            'entered_amount', 'total_amount', 'entry_add_time',
            'request_status', 'confirm_request_accept_date_time',
            'state', 'district', 'taluka', 'village'
        ]

    # Custom methods to retrieve related object details
    def get_bank_name(self, obj):
        return obj.bank.bank_name if obj.bank else None

    def get_user_name(self, obj):
        return obj.user.full_name if obj.user else None

    def get_agent_name(self, obj):
        return obj.agent.agent_name if obj.agent else None


# UserLoanAddStatement Serializer


class UserLoanAddStatementSerializer(serializers.ModelSerializer):
    bank_id = serializers.PrimaryKeyRelatedField(
        queryset=Bank.objects.all(), source='bank'
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=UserDetail.objects.all(), source='user'
    )

    # Additional fields for better readability
    bank_name = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = UserLoanAddStatement
        fields = [
            'id', 'bank_id', 'user_id', 'bank_name', 'user_name',
            'loan_amount', 'loan_date', 'loan_type', 'loan_status',
            'interest_rate', 'repayment_period', 'state', 'district',
            'taluka', 'village'
        ]

    def get_bank_name(self, obj):
        return obj.bank.name if obj.bank else None

    def get_user_name(self, obj):
        return obj.user.full_name if obj.user else None


# UserLoanStatement Serializer


class UserLoanStatementSerializer(serializers.ModelSerializer):
    # PrimaryKey fields for relational data
    bank_id = serializers.PrimaryKeyRelatedField(
        queryset=Bank.objects.all(), source='bank'
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=UserDetail.objects.all(), source='user'
    )

    # Additional fields for better readability
    bank_name = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = UserLoanStatement
        fields = [
            'id', 'bank_id', 'user_id', 'bank_name', 'user_name',
            'loan_amount', 'outstanding_amount', 'loan_type', 'loan_status',
            'interest_rate', 'repayment_start_date', 'repayment_end_date',
            'state', 'district', 'taluka', 'village'
        ]

    # Methods for custom fields
    def get_bank_name(self, obj):
        return obj.bank.name if obj.bank else None

    def get_user_name(self, obj):
        return obj.user.full_name if obj.user else None


# BankPrivacyPolicy Serializer


class BankPrivacyPolicySerializer(serializers.ModelSerializer, BaseLocationSerializerMixin):
    # PrimaryKey field for relational data
    bank_id = serializers.PrimaryKeyRelatedField(
        queryset=Bank.objects.all(), source='bank'
    )

    # Additional field for better readability
    bank_name = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    district = serializers.SerializerMethodField()
    taluka = serializers.SerializerMethodField()
    village = serializers.SerializerMethodField()

    class Meta:
        model = BankPrivacyPolicy
        fields = '__all__'

    # Custom method for retrieving bank name
    def get_bank_name(self, obj):
        return obj.bank.bank_name if obj.bank else None


# BankAbout Serializer


class BankAboutSerializer(serializers.ModelSerializer, BaseLocationSerializerMixin):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())
    bank_name = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    district = serializers.SerializerMethodField()
    taluka = serializers.SerializerMethodField()
    village = serializers.SerializerMethodField()

    class Meta:
        model = BankAbout
        fields = '__all__'
     # Custom method for retrieving bank name

    def get_bank_name(self, obj):
        return obj.bank.bank_name if obj.bank else None
