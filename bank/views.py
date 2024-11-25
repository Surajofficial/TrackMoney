from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from .filters import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Bank CRUD Views
from django.core.cache import cache
import random
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated


def get_tokens_for_user(user, user_type):
    refresh = RefreshToken.for_user(user)
    refresh['user_type'] = user_type
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def generate_otp(contact_number):
    otp = random.randint(100000, 999999)  # Generate 6-digit OTP
    # Store OTP with 5-minute expiration
    cache.set(contact_number, otp, timeout=300)
    # Implement sending OTP via SMS or Email here
    print(f"OTP for {contact_number} is {otp}")  # For testing, print the OTP
    return otp


class SendOTPView(APIView):
    def post(self, request):
        contact_number = request.data.get("contact_number")
        if not contact_number:
            return Response({'error': 'Contact number is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate and send OTP
        otp = generate_otp(contact_number)
        return Response({'message': f'OTP sent successfully {otp}'}, status=status.HTTP_200_OK)


class BankLoginView(APIView):
    def post(self, request):
        serializer = BankLoginSerializer(data=request.data)
        if serializer.is_valid():
            contact_number = serializer.validated_data['contact_number']
            otp = serializer.validated_data['otp']

            try:
                bank_user = Bank.objects.filter(
                    contact_number=contact_number).first()
                # Replace with actual OTP verification
                cached_otp = cache.get(contact_number)
                # return Response(cached_otp, status=status.HTTP_200_OK)
                # Assuming '123456' is the correct OTP for demonstration
                if cached_otp and str(cached_otp) == otp:
                    tokens = get_tokens_for_user(bank_user, user_type='bank')

                    return Response(tokens, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
            except Bank.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AgentLoginView(APIView):
    def post(self, request):
        serializer = AgentLoginSerializer(data=request.data)
        if serializer.is_valid():
            contact_number = serializer.validated_data['contact_number']
            otp = serializer.validated_data['otp']

            try:
                agent_user = Agent.objects.get(contact_number=contact_number)
                cached_otp = cache.get(contact_number)
                if cached_otp and str(cached_otp) == otp:
                    tokens = get_tokens_for_user(agent_user, user_type='agent')
                    return Response(tokens, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
            except Agent.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailLoginView(APIView):
    def post(self, request):
        serializer = UserDetailLoginSerializer(data=request.data)
        if serializer.is_valid():
            contact_number = serializer.validated_data['contact_number']
            otp = serializer.validated_data['otp']

            try:
                user_detail = UserDetail.objects.get(
                    contact_number=contact_number)
                cached_otp = cache.get(contact_number)
                if cached_otp and str(cached_otp) == otp:
                    tokens = get_tokens_for_user(
                        user_detail, user_type='user_detail')
                    return Response(tokens, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
            except UserDetail.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BaseListCreateView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        # Order by a default field in descending order
        return self.queryset.order_by('-id')


class BaseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    pass


class BankListCreateView(BaseListCreateView):
    permission_classes = [IsAuthenticated]
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    filterset_class = BankFilter


class BankRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    permission_classes = [IsAuthenticated]
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

# Agent CRUD Views


class AgentListCreateView(BaseListCreateView):
    permission_classes = [IsAuthenticated]
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    filterset_class = AgentFilter


class AgentRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    permission_classes = [IsAuthenticated]
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

# User Detail CRUD Views


class UserDetailListCreateView(BaseListCreateView):
    permission_classes = [IsAuthenticated]
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    filterset_class = UserDetailFilter


class UserDetailRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    permission_classes = [IsAuthenticated]
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer

# Agent Assigned to Bank CRUD Views


class AgentAssignedToBankListCreateView(BaseListCreateView):
    permission_classes = [IsAuthenticated]
    queryset = AgentAssignedToBank.objects.all()
    serializer_class = AgentAssignedToBankSerializer
    filterset_class = AgentAssignedToBankFilter


class AgentAssignedToBankRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    permission_classes = [IsAuthenticated]
    queryset = AgentAssignedToBank.objects.all()
    serializer_class = AgentAssignedToBankSerializer

# User Assigned to Bank CRUD Views


class UserAssignedToBankListCreateView(BaseListCreateView):
    permission_classes = [IsAuthenticated]
    queryset = UserAssignedToBank.objects.all()
    serializer_class = UserAssignedToBankSerializer
    filterset_class = UserAssignedToBankFilter


class UserAssignedToBankRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    permission_classes = [IsAuthenticated]
    queryset = UserAssignedToBank.objects.all()
    serializer_class = UserAssignedToBankSerializer

# User Payment Statement CRUD Views


class UserPaymentStatementListCreateView(BaseListCreateView):
    permission_classes = [IsAuthenticated]
    queryset = UserPaymentStatement.objects.all()
    serializer_class = UserPaymentStatementSerializer
    filterset_class = UserPaymentStatementFilter


class UserPaymentStatementRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    permission_classes = [IsAuthenticated]
    queryset = UserPaymentStatement.objects.all()
    serializer_class = UserPaymentStatementSerializer

# User Loan Add Statement CRUD Views


class UserLoanAddStatementListCreateView(BaseListCreateView):
    permission_classes = [IsAuthenticated]
    queryset = UserLoanAddStatement.objects.all()
    serializer_class = UserLoanAddStatementSerializer
    filterset_class = UserLoanAddStatementFilter


class UserLoanAddStatementRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    permission_classes = [IsAuthenticated]
    queryset = UserLoanAddStatement.objects.all()
    serializer_class = UserLoanAddStatementSerializer

# User Loan Statement CRUD Views


class UserLoanStatementListCreateView(BaseListCreateView):
    permission_classes = [IsAuthenticated]
    queryset = UserLoanStatement.objects.all()
    serializer_class = UserLoanStatementSerializer
    filterset_class = UserLoanStatementFilter


class UserLoanStatementRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    permission_classes = [IsAuthenticated]
    queryset = UserLoanStatement.objects.all()
    serializer_class = UserLoanStatementSerializer

# Bank Privacy Policy CRUD Views


class BankPrivacyPolicyListCreateView(BaseListCreateView):
    permission_classes = [IsAuthenticated]
    queryset = BankPrivacyPolicy.objects.all()
    serializer_class = BankPrivacyPolicySerializer
    filterset_class = BankPrivacyPolicyFilter


class BankPrivacyPolicyRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    permission_classes = [IsAuthenticated]
    queryset = BankPrivacyPolicy.objects.all()
    serializer_class = BankPrivacyPolicySerializer

# Bank About CRUD Views


class BankAboutListCreateView(BaseListCreateView):
    permission_classes = [IsAuthenticated]
    queryset = BankAbout.objects.all()
    serializer_class = BankAboutSerializer
    filterset_class = BankAboutFilter


class BankAboutRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    permission_classes = [IsAuthenticated]
    queryset = BankAbout.objects.all()
    serializer_class = BankAboutSerializer

# State CRUD Views


class StateListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = State.objects.all()
    serializer_class = StateSerializer

# District CRUD Views


class DistrictListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class DistrictRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

# Taluka CRUD Views


class TalukaListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Taluka.objects.all()
    serializer_class = TalukaSerializer


class TalukaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Taluka.objects.all()
    serializer_class = TalukaSerializer

# Village CRUD Views


class VillageListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Village.objects.all()
    serializer_class = VillageSerializer


class VillageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
