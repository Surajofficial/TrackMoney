from rest_framework import serializers
from .models import *


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

    class Meta:
        model = Taluka
        fields = ['id', 'name', 'state', 'district']


class VillageSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    taluka = TalukaSerializer(read_only=True)

    class Meta:
        model = Village
        fields = ['id', 'name', 'state', 'district', 'taluka']

# Helper function to get name attributes


def get_name_field(obj, field_name):
    return getattr(obj, field_name).name if getattr(obj, field_name) else None


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
        fields = ['id', 'name', 'state_id', 'district_id', 'taluka_id',
                  'village_id', 'state', 'district', 'taluka', 'village']

    def get_state(self, obj):
        return get_name_field(obj, 'state')

    def get_district(self, obj):
        return get_name_field(obj, 'district')

    def get_taluka(self, obj):
        return get_name_field(obj, 'taluka')

    def get_village(self, obj):
        return get_name_field(obj, 'village')


class AgentSerializer(serializers.ModelSerializer):
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

    def get_state(self, obj):
        return get_name_field(obj, 'state')

    def get_district(self, obj):
        return get_name_field(obj, 'district')

    def get_taluka(self, obj):
        return get_name_field(obj, 'taluka')

    def get_village(self, obj):
        return get_name_field(obj, 'village')


class UserDetailSerializer(serializers.ModelSerializer):
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

    def get_state(self, obj):
        return get_name_field(obj, 'state')

    def get_district(self, obj):
        return get_name_field(obj, 'district')

    def get_taluka(self, obj):
        return get_name_field(obj, 'taluka')

    def get_village(self, obj):
        return get_name_field(obj, 'village')


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
