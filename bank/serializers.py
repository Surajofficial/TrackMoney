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
    state = StateSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    state = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(), source='state')
    district = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all(), source='district')

    class Meta:
        model = Taluka
        fields = ['id', 'name', 'state', 'district']


class VillageSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    taluka = TalukaSerializer(read_only=True)
    state = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(), source='state')
    district = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all(), source='district')
    taluka = serializers.PrimaryKeyRelatedField(
        queryset=Taluka.objects.all(), source='taluka')

    class Meta:
        model = Village
        fields = ['id', 'name', 'state', 'district', 'taluka']

# Bank Serializer with dynamic fields for fetching data


class BankSerializer(serializers.ModelSerializer):
    state = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all())
    district = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all())
    taluka = serializers.PrimaryKeyRelatedField(
        queryset=Taluka.objects.all())
    village = serializers.PrimaryKeyRelatedField(
        queryset=Village.objects.all())

    # Read-only fields to include details when fetching data
    state_name = serializers.SerializerMethodField()
    district_name = serializers.SerializerMethodField()
    taluka_name = serializers.SerializerMethodField()
    village_name = serializers.SerializerMethodField()

    class Meta:
        model = Bank
        fields = '__all__'

    def get_state_name(self, obj):
        return obj.state.name if obj.state else None

    def get_district_name(self, obj):
        return obj.district.name if obj.district else None

    def get_taluka_name(self, obj):
        return obj.taluka.name if obj.taluka else None

    def get_village_name(self, obj):
        return obj.village.name if obj.village else None

# Agent Serializer


class AgentSerializer(serializers.ModelSerializer):
    state = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all())
    district = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all())
    taluka = serializers.PrimaryKeyRelatedField(
        queryset=Taluka.objects.all())
    village = serializers.PrimaryKeyRelatedField(
        queryset=Village.objects.all())

    state_name = serializers.SerializerMethodField()
    district_name = serializers.SerializerMethodField()
    taluka_name = serializers.SerializerMethodField()
    village_name = serializers.SerializerMethodField()

    class Meta:
        model = Agent
        fields = [
            'id', 'agent_name', 'state', 'district', 'taluka', 'village',
            'state_name', 'district_name', 'taluka_name', 'village_name',
            'address', 'contact_number', 'uid_number', 'birth_date', 'photo', 'uid_doc'
        ]

    def get_state_name(self, obj):
        return obj.state.name if obj.state else None

    def get_district_name(self, obj):
        return obj.district.name if obj.district else None

    def get_taluka_name(self, obj):
        return obj.taluka.name if obj.taluka else None

    def get_village_name(self, obj):
        return obj.village.name if obj.village else None

# UserDetail Serializer


class UserDetailSerializer(serializers.ModelSerializer):
    state = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all())
    district = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all())
    taluka = serializers.PrimaryKeyRelatedField(
        queryset=Taluka.objects.all())
    village = serializers.PrimaryKeyRelatedField(
        queryset=Village.objects.all())

    state_name = serializers.SerializerMethodField()
    district_name = serializers.SerializerMethodField()
    taluka_name = serializers.SerializerMethodField()
    village_name = serializers.SerializerMethodField()

    class Meta:
        model = UserDetail
        fields = '__all__'

    def get_state_name(self, obj):
        return obj.state.name if obj.state else None

    def get_district_name(self, obj):
        return obj.district.name if obj.district else None

    def get_taluka_name(self, obj):
        return obj.taluka.name if obj.taluka else None

    def get_village_name(self, obj):
        return obj.village.name if obj.village else None

# AgentAssignedToBank Serializer


class AgentAssignedToBankSerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())
    agent = serializers.PrimaryKeyRelatedField(queryset=Agent.objects.all())

    class Meta:
        model = AgentAssignedToBank
        fields = '__all__'

# UserAssignedToBank Serializer


class UserAssignedToBankSerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())
    user = serializers.PrimaryKeyRelatedField(
        queryset=UserDetail.objects.all())

    class Meta:
        model = UserAssignedToBank
        fields = '__all__'

# UserPaymentStatement Serializer


class UserPaymentStatementSerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())
    user = serializers.PrimaryKeyRelatedField(
        queryset=UserDetail.objects.all())
    agent = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.all(), allow_null=True, required=False)

    class Meta:
        model = UserPaymentStatement
        fields = '__all__'

# UserLoanAddStatement Serializer


class UserLoanAddStatementSerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())
    user = serializers.PrimaryKeyRelatedField(
        queryset=UserDetail.objects.all())

    class Meta:
        model = UserLoanAddStatement
        fields = '__all__'

# UserLoanStatement Serializer


class UserLoanStatementSerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())
    user = serializers.PrimaryKeyRelatedField(
        queryset=UserDetail.objects.all())

    class Meta:
        model = UserLoanStatement
        fields = '__all__'

# BankPrivacyPolicy Serializer


class BankPrivacyPolicySerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())

    class Meta:
        model = BankPrivacyPolicy
        fields = '__all__'

# BankAbout Serializer


class BankAboutSerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())

    class Meta:
        model = BankAbout
        fields = '__all__'
