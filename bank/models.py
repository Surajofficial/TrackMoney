from django.db import models

# State and District models


class State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name="districts")

    def __str__(self):
        return f"{self.name} ({self.state.name})"


class LocationBase(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    taluka = models.CharField(max_length=100)
    village = models.CharField(max_length=100)

    class Meta:
        abstract = True  # This will make it a base class without a database table


# Bank model inheriting LocationBase
class Bank(LocationBase):
    bank_name = models.CharField(max_length=255)
    address = models.TextField()
    bank_manager = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    pin_code = models.CharField(max_length=6)
    bank_logo = models.FileField(upload_to='media/bank_logos/')

    def __str__(self):
        return self.bank_name


# Agent model inheriting LocationBase
class Agent(LocationBase):
    agent_name = models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    uid_number = models.CharField(max_length=12)
    birth_date = models.DateField()
    photo = models.FileField(upload_to='media/agent_photos/')
    uid_doc = models.FileField(upload_to='media/agent_uid_docs/')

    def __str__(self):
        return self.agent_name


# UserDetail model inheriting LocationBase
class UserDetail(LocationBase):
    full_name = models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    pin_code = models.CharField(max_length=6)
    uid_number = models.CharField(max_length=12)
    uid_doc = models.FileField(upload_to='media/user_uid_docs/')
    user_photo = models.FileField(upload_to='media/user_photos/')
    business_name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=255)  # Dropdown in frontend

    def __str__(self):
        return self.full_name


# AgentAssignedToBank model inheriting LocationBase
class AgentAssignedToBank(LocationBase):
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE, related_name="assigned_agents")
    agent = models.ForeignKey(
        Agent, on_delete=models.CASCADE, related_name="assigned_banks")


# UserAssignedToBank model inheriting LocationBase
class UserAssignedToBank(LocationBase):
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE, related_name="assigned_users")
    user = models.ForeignKey(
        UserDetail, on_delete=models.CASCADE, related_name="assigned_banks")


# UserPaymentStatement model inheriting LocationBase
class UserPaymentStatement(LocationBase):
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE, related_name="payment_statements")
    user = models.ForeignKey(
        UserDetail, on_delete=models.CASCADE, related_name="payment_statements")
    # e.g., add/withdraw/loan EMI
    amount_type = models.CharField(max_length=50)
    yesterday_total_amount = models.DecimalField(
        max_digits=10, decimal_places=2)
    entered_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    agent = models.ForeignKey(
        Agent, on_delete=models.SET_NULL, null=True, blank=True, related_name="payment_statements")
    entry_add_time = models.DateTimeField()
    request_status = models.BooleanField(default=False)
    confirm_request_accept_date_time = models.DateTimeField(
        null=True, blank=True)


# UserLoanAddStatement model inheriting LocationBase
class UserLoanAddStatement(LocationBase):
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE, related_name="loan_add_statements")
    user = models.ForeignKey(
        UserDetail, on_delete=models.CASCADE, related_name="loan_add_statements")
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    emi = models.IntegerField()
    remaining_loan = models.DecimalField(max_digits=10, decimal_places=2)
    loan_close_date = models.DateField()
    agreement_copy = models.FileField(
        upload_to='media/loan_agreements/', null=True, blank=True)


# UserLoanStatement model inheriting LocationBase
class UserLoanStatement(LocationBase):
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE, related_name="loan_statements")
    user = models.ForeignKey(
        UserDetail, on_delete=models.CASCADE, related_name="loan_statements")
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    emi = models.IntegerField()
    emi_add_type = models.CharField(max_length=50)  # e.g., account/cash-online
    added_emi_amount = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_loan = models.DecimalField(max_digits=10, decimal_places=2)


# BankPrivacyPolicy model inheriting LocationBase
class BankPrivacyPolicy(LocationBase):
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE, related_name="privacy_policies")
    policy_doc = models.FileField(upload_to='media/bank_privacy_policies/')


# BankAbout model inheriting LocationBase
class BankAbout(LocationBase):
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE, related_name="about_info")
    about_doc = models.FileField(upload_to='media/bank_about_docs/')
