from django_filters import rest_framework as filters
from .models import *


class BaseFilter(filters.FilterSet):
    class Meta:
        fields = '__all__'  # Apply filtering on all fields
        exclude = []  # Leave empty here to exclude fields on a per-model basis

        # Define filter overrides to ignore media fields globally
        filter_overrides = {
            models.FileField: {
                'filter_class': filters.CharFilter,
                # Exclude FileField from filtering
                'extra': lambda f: {'lookup_expr': 'exact', 'exclude': True}
            },
            models.ImageField: {
                'filter_class': filters.CharFilter,
                # Exclude ImageField from filtering
                'extra': lambda f: {'lookup_expr': 'exact', 'exclude': True}
            },
        }


class BankFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Bank


class AgentFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = Agent


class UserDetailFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = UserDetail


class AgentAssignedToBankFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = AgentAssignedToBank


class UserAssignedToBankFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = UserAssignedToBank


class UserPaymentStatementFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = UserPaymentStatement


class UserLoanAddStatementFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = UserLoanAddStatement


class UserLoanStatementFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = UserLoanStatement


class BankPrivacyPolicyFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = BankPrivacyPolicy


class BankAboutFilter(BaseFilter):
    class Meta(BaseFilter.Meta):
        model = BankAbout  # Assuming you meant `BankAbout` here
