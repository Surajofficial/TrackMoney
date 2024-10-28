from rest_framework import serializers
from .models import (
    Bank, Agent, UserDetail, AgentAssignedToBank, UserAssignedToBank,
    UserPaymentStatement, UserLoanAddStatement, UserLoanStatement,
    BankPrivacyPolicy, BankAbout, State, District
)

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


# Main serializers with select2 compatible fields

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
