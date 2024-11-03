from rest_framework import serializers
from .models import *

# State and District serializers to use as nested serializers


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name']


class DistrictSerializer(serializers.ModelSerializer):
    # Include state details as nested serializer
    state = StateSerializer(read_only=True)

    class Meta:
        model = District
        fields = ['id', 'name', 'state']
class TalukaSerializer(serializers.ModelSerializer):
    # Include state and district details as nested serializers for read-only display
    state = StateSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    # Allow setting state and district by ID
    state_id = serializers.PrimaryKeyRelatedField(queryset=State.objects.all(), source='state')
    district_id = serializers.PrimaryKeyRelatedField(queryset=District.objects.all(), source='district')

    class Meta:
        model = Taluka
        fields = ['id', 'name', 'state', 'state_id', 'district', 'district_id'] 
class VillageSerializer(serializers.ModelSerializer):
    # Include state, district, and taluka details as nested serializers for read-only display
    state = StateSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    taluka = TalukaSerializer(read_only=True)

    # Writable fields to set state, district, and taluka by ID
    state_id = serializers.PrimaryKeyRelatedField(queryset=State.objects.all(), source='state')
    district_id = serializers.PrimaryKeyRelatedField(queryset=District.objects.all(), source='district')
    taluka_id = serializers.PrimaryKeyRelatedField(queryset=Taluka.objects.all(), source='taluka')

    class Meta:
        model = Village
        fields = ['id', 'name', 'state', 'state_id', 'district', 'district_id', 'taluka', 'taluka_id']
class BankSerializer(serializers.ModelSerializer):
    state = serializers.PrimaryKeyRelatedField(queryset=State.objects.all())
    district = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all())

    class Meta:
        model = Bank
        fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
    state = serializers.PrimaryKeyRelatedField(queryset=State.objects.all())
    district = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all())

    class Meta:
        model = Agent
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    state = serializers.PrimaryKeyRelatedField(queryset=State.objects.all())
    district = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all())

    class Meta:
        model = UserDetail
        fields = '__all__'


class AgentAssignedToBankSerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())
    agent = serializers.PrimaryKeyRelatedField(queryset=Agent.objects.all())

    class Meta:
        model = AgentAssignedToBank
        fields = '__all__'


class UserAssignedToBankSerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())
    user = serializers.PrimaryKeyRelatedField(
        queryset=UserDetail.objects.all())

    class Meta:
        model = UserAssignedToBank
        fields = '__all__'


class UserPaymentStatementSerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())
    user = serializers.PrimaryKeyRelatedField(
        queryset=UserDetail.objects.all())
    agent = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.all(), allow_null=True, required=False)

    class Meta:
        model = UserPaymentStatement
        fields = '__all__'


class UserLoanAddStatementSerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())
    user = serializers.PrimaryKeyRelatedField(
        queryset=UserDetail.objects.all())

    class Meta:
        model = UserLoanAddStatement
        fields = '__all__'


class UserLoanStatementSerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())
    user = serializers.PrimaryKeyRelatedField(
        queryset=UserDetail.objects.all())

    class Meta:
        model = UserLoanStatement
        fields = '__all__'


class BankPrivacyPolicySerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())

    class Meta:
        model = BankPrivacyPolicy
        fields = '__all__'


class BankAboutSerializer(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())

    class Meta:
        model = BankAbout
        fields = '__all__'
