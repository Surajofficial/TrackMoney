from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from .filters import *
# Bank CRUD Views


class BaseListCreateView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        # Order by a default field in descending order
        return self.queryset.order_by('-id')


class BaseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    pass


class BankListCreateView(BaseListCreateView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    filterset_class = BankFilter


class BankRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

# Agent CRUD Views


class AgentListCreateView(BaseListCreateView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    filterset_class = AgentFilter


class AgentRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

# User Detail CRUD Views


class UserDetailListCreateView(BaseListCreateView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    filterset_class = UserDetailFilter


class UserDetailRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer

# Agent Assigned to Bank CRUD Views


class AgentAssignedToBankListCreateView(BaseListCreateView):
    queryset = AgentAssignedToBank.objects.all()
    serializer_class = AgentAssignedToBankSerializer
    filterset_class = AgentAssignedToBankFilter


class AgentAssignedToBankRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = AgentAssignedToBank.objects.all()
    serializer_class = AgentAssignedToBankSerializer

# User Assigned to Bank CRUD Views


class UserAssignedToBankListCreateView(BaseListCreateView):
    queryset = UserAssignedToBank.objects.all()
    serializer_class = UserAssignedToBankSerializer
    filterset_class = UserAssignedToBankFilter


class UserAssignedToBankRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = UserAssignedToBank.objects.all()
    serializer_class = UserAssignedToBankSerializer

# User Payment Statement CRUD Views


class UserPaymentStatementListCreateView(BaseListCreateView):
    queryset = UserPaymentStatement.objects.all()
    serializer_class = UserPaymentStatementSerializer
    filterset_class = UserPaymentStatementFilter


class UserPaymentStatementRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = UserPaymentStatement.objects.all()
    serializer_class = UserPaymentStatementSerializer

# User Loan Add Statement CRUD Views


class UserLoanAddStatementListCreateView(BaseListCreateView):
    queryset = UserLoanAddStatement.objects.all()
    serializer_class = UserLoanAddStatementSerializer
    filterset_class = UserLoanAddStatementFilter


class UserLoanAddStatementRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = UserLoanAddStatement.objects.all()
    serializer_class = UserLoanAddStatementSerializer

# User Loan Statement CRUD Views


class UserLoanStatementListCreateView(BaseListCreateView):
    queryset = UserLoanStatement.objects.all()
    serializer_class = UserLoanStatementSerializer
    filterset_class = UserLoanStatementFilter


class UserLoanStatementRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = UserLoanStatement.objects.all()
    serializer_class = UserLoanStatementSerializer

# Bank Privacy Policy CRUD Views


class BankPrivacyPolicyListCreateView(BaseListCreateView):
    queryset = BankPrivacyPolicy.objects.all()
    serializer_class = BankPrivacyPolicySerializer
    filterset_class = BankPrivacyPolicyFilter


class BankPrivacyPolicyRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = BankPrivacyPolicy.objects.all()
    serializer_class = BankPrivacyPolicySerializer

# Bank About CRUD Views


class BankAboutListCreateView(BaseListCreateView):
    queryset = BankAbout.objects.all()
    serializer_class = BankAboutSerializer
    filterset_class = BankAboutFilter


class BankAboutRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = BankAbout.objects.all()
    serializer_class = BankAboutSerializer

# State CRUD Views
class StateListCreateView(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

# District CRUD Views
class DistrictListCreateView(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class DistrictRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

# Taluka CRUD Views
class TalukaListCreateView(generics.ListCreateAPIView):
    queryset = Taluka.objects.all()
    serializer_class = TalukaSerializer

class TalukaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Taluka.objects.all()
    serializer_class = TalukaSerializer

# Village CRUD Views
class VillageListCreateView(generics.ListCreateAPIView):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer

class VillageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer