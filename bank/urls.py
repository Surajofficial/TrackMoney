from django.urls import path
from .views import *

urlpatterns = [
    # Bank CRUD Endpoints
    path('banks/', BankListCreateView.as_view(), name='bank-list-create'),
    path('banks/<int:pk>/', BankRetrieveUpdateDestroyView.as_view(),
         name='bank-detail'),

    # Agent CRUD Endpoints
    path('agents/', AgentListCreateView.as_view(), name='agent-list-create'),
    path('agents/<int:pk>/', AgentRetrieveUpdateDestroyView.as_view(),
         name='agent-detail'),

    # User Detail CRUD Endpoints
    path('user-details/', UserDetailListCreateView.as_view(),
         name='user-detail-list-create'),
    path('user-details/<int:pk>/',
         UserDetailRetrieveUpdateDestroyView.as_view(), name='user-detail'),

    # Agent Assigned to Bank CRUD Endpoints
    path('agent-assigned-to-bank/', AgentAssignedToBankListCreateView.as_view(),
         name='agent-assigned-list-create'),
    path('agent-assigned-to-bank/<int:pk>/',
         AgentAssignedToBankRetrieveUpdateDestroyView.as_view(), name='agent-assigned-detail'),

    # User Assigned to Bank CRUD Endpoints
    path('user-assigned-to-bank/', UserAssignedToBankListCreateView.as_view(),
         name='user-assigned-list-create'),
    path('user-assigned-to-bank/<int:pk>/',
         UserAssignedToBankRetrieveUpdateDestroyView.as_view(), name='user-assigned-detail'),

    # User Payment Statement CRUD Endpoints
    path('user-payment-statement/', UserPaymentStatementListCreateView.as_view(),
         name='user-payment-statement-list-create'),
    path('user-payment-statement/<int:pk>/',
         UserPaymentStatementRetrieveUpdateDestroyView.as_view(), name='user-payment-statement-detail'),

    # User Loan Add Statement CRUD Endpoints
    path('user-loan-add-statement/', UserLoanAddStatementListCreateView.as_view(),
         name='user-loan-add-list-create'),
    path('user-loan-add-statement/<int:pk>/',
         UserLoanAddStatementRetrieveUpdateDestroyView.as_view(), name='user-loan-add-detail'),

    # User Loan Statement CRUD Endpoints
    path('user-loan-statement/', UserLoanStatementListCreateView.as_view(),
         name='user-loan-statement-list-create'),
    path('user-loan-statement/<int:pk>/',
         UserLoanStatementRetrieveUpdateDestroyView.as_view(), name='user-loan-statement-detail'),

    # Bank Privacy Policy CRUD Endpoints
    path('bank-privacy-policy/', BankPrivacyPolicyListCreateView.as_view(),
         name='bank-privacy-policy-list-create'),
    path('bank-privacy-policy/<int:pk>/',
         BankPrivacyPolicyRetrieveUpdateDestroyView.as_view(), name='bank-privacy-policy-detail'),

    # Bank About CRUD Endpoints
    path('bank-about/', BankAboutListCreateView.as_view(),
         name='bank-about-list-create'),
    path('bank-about/<int:pk>/',
         BankAboutRetrieveUpdateDestroyView.as_view(), name='bank-about-detail'),
         path('states/', StateListCreateView.as_view(), name='state-list-create'),
    path('states/<int:pk>/', StateRetrieveUpdateDestroyView.as_view(), name='state-detail'),

    # District URLs
    path('districts/', DistrictListCreateView.as_view(), name='district-list-create'),
    path('districts/<int:pk>/', DistrictRetrieveUpdateDestroyView.as_view(), name='district-detail'),

    # Taluka URLs
    path('talukas/', TalukaListCreateView.as_view(), name='taluka-list-create'),
    path('talukas/<int:pk>/', TalukaRetrieveUpdateDestroyView.as_view(), name='taluka-detail'),

    # Village URLs
    path('villages/', VillageListCreateView.as_view(), name='village-list-create'),
    path('villages/<int:pk>/', VillageRetrieveUpdateDestroyView.as_view(), name='village-detail'),
]
