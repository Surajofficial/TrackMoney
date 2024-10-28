from rest_framework import generics
from dal import autocomplete
from .models import (
    Bank, Agent, UserDetail, AgentAssignedToBank, UserAssignedToBank,
    UserPaymentStatement, UserLoanAddStatement, UserLoanStatement,
    BankPrivacyPolicy, BankAbout, District, State
)
from .serializers import (
    BankSerializer, AgentSerializer, UserDetailSerializer,
    AgentAssignedToBankSerializer, UserAssignedToBankSerializer,
    UserPaymentStatementSerializer, UserLoanAddStatementSerializer,
    UserLoanStatementSerializer, BankPrivacyPolicySerializer,
    BankAboutSerializer
)

# Bank CRUD Views


class BankListCreateView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

# Agent CRUD Views


class AgentListCreateView(generics.ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class AgentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

# User Detail CRUD Views


class UserDetailListCreateView(generics.ListCreateAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer


class UserDetailRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer

# Agent Assigned to Bank CRUD Views


class AgentAssignedToBankListCreateView(generics.ListCreateAPIView):
    queryset = AgentAssignedToBank.objects.all()
    serializer_class = AgentAssignedToBankSerializer


class AgentAssignedToBankRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgentAssignedToBank.objects.all()
    serializer_class = AgentAssignedToBankSerializer

# User Assigned to Bank CRUD Views


class UserAssignedToBankListCreateView(generics.ListCreateAPIView):
    queryset = UserAssignedToBank.objects.all()
    serializer_class = UserAssignedToBankSerializer


class UserAssignedToBankRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAssignedToBank.objects.all()
    serializer_class = UserAssignedToBankSerializer

# User Payment Statement CRUD Views


class UserPaymentStatementListCreateView(generics.ListCreateAPIView):
    queryset = UserPaymentStatement.objects.all()
    serializer_class = UserPaymentStatementSerializer


class UserPaymentStatementRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserPaymentStatement.objects.all()
    serializer_class = UserPaymentStatementSerializer

# User Loan Add Statement CRUD Views


class UserLoanAddStatementListCreateView(generics.ListCreateAPIView):
    queryset = UserLoanAddStatement.objects.all()
    serializer_class = UserLoanAddStatementSerializer


class UserLoanAddStatementRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserLoanAddStatement.objects.all()
    serializer_class = UserLoanAddStatementSerializer

# User Loan Statement CRUD Views


class UserLoanStatementListCreateView(generics.ListCreateAPIView):
    queryset = UserLoanStatement.objects.all()
    serializer_class = UserLoanStatementSerializer


class UserLoanStatementRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserLoanStatement.objects.all()
    serializer_class = UserLoanStatementSerializer

# Bank Privacy Policy CRUD Views


class BankPrivacyPolicyListCreateView(generics.ListCreateAPIView):
    queryset = BankPrivacyPolicy.objects.all()
    serializer_class = BankPrivacyPolicySerializer


class BankPrivacyPolicyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BankPrivacyPolicy.objects.all()
    serializer_class = BankPrivacyPolicySerializer

# Bank About CRUD Views


class BankAboutListCreateView(generics.ListCreateAPIView):
    queryset = BankAbout.objects.all()
    serializer_class = BankAboutSerializer


class BankAboutRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BankAbout.objects.all()
    serializer_class = BankAboutSerializer
