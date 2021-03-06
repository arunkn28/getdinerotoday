from django.db import models
from django.utils import timezone
from user.models import Profile


class ModelMixin:
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)


class Domain(ModelMixin, models.Model):
    class Meta:
        db_table = 'domain'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    domain_name = models.CharField(max_length=50)
    domain_needed = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class EquipmentFinancing(ModelMixin, models.Model):
    class Meta:
        db_table = 'equipment_financing'
    lender_name = models.CharField(max_length=50)
    personal_credit_score = models.CharField(max_length=50)
    time_in_business = models.CharField(max_length=50)
    business_revenue = models.CharField(max_length=15)
    term_length = models.CharField(max_length=10)
    apr = models.CharField(max_length=10)
    strategy = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class Fax(ModelMixin, models.Model):
    class Meta:
        db_table = 'fax'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fax_needed = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50)
    updated_at = models.DateTimeField(null=True, blank=True)


class InvoiceFactoring(ModelMixin, models.Model):
    class Meta:
        db_table = 'invoice_factoring'
    lender_name = models.CharField(max_length=50)
    personal_credit_score = models.CharField(max_length=50)
    time_in_business = models.CharField(max_length=50)
    business_revenue = models.CharField(max_length=15)
    term_length = models.CharField(max_length=10)
    apr = models.CharField(max_length=10)
    strategy = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class InvoiceFinancing(ModelMixin, models.Model):
    class Meta:
        db_table = 'invoice_financing'

    lender_name = models.CharField(max_length=50)
    personal_credit_score = models.CharField(max_length=50)
    time_in_business = models.CharField(max_length=50)
    business_revenue = models.CharField(max_length=15)
    term_length = models.CharField(max_length=10)
    apr = models.CharField(max_length=10)
    strategy = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class Category(models.Model):
    class Meta:
        db_table = 'category'
    title = models.CharField(max_length=50)


class Lender(ModelMixin, models.Model):
    class Meta:
        db_table = 'lender'
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=500, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    report_to = models.CharField(max_length=50, null=True)
    monthly_payment = models.CharField(max_length=15, null=True)
    estimated_term = models.CharField(max_length=50, null=True)
    estimated_amount = models.CharField(max_length=5, null=True)
    payment_terms = models.CharField(max_length=50, null=True)
    terms = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class LinesOfCredit(ModelMixin, models.Model):
    class Meta:
        db_table = 'lines_of_credit'

    lender_name = models.CharField(max_length=50)
    personal_credit_score = models.CharField(max_length=50)
    time_in_business = models.CharField(max_length=50)
    business_revenue = models.CharField(max_length=15)
    term_length = models.CharField(max_length=10)
    apr = models.CharField(max_length=10)
    strategy = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class Nopg(ModelMixin, models.Model):
    class Meta:
        db_table = 'nopg'
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    report_to = models.CharField(max_length=50)
    monthly_payment = models.CharField(max_length=15)
    estimated_term = models.DateField()
    payment_terms = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class ProfessionalEmailAddress(ModelMixin, models.Model):
    class Meta:
        db_table = 'professional_email_address'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    email_address_needed = models.CharField(max_length=50)
    domain_present = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class Progress(ModelMixin, models.Model):
    class Meta:
        db_table = 'progress'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    website_creation = models.CharField(max_length=50)
    dns_number = models.CharField(max_length=50)
    virtual_number = models.CharField(max_length=50)
    fax_number = models.CharField(max_length=50)
    toll_free_number = models.CharField(max_length=50)
    business_bank_account = models.CharField(max_length=50)
    listing = models.CharField(max_length=50)
    professional_email_address = models.CharField(max_length=50)
    domain = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class Industry(models.Model):
    class Meta:
        db_table = 'industry'
    title = models.CharField(max_length=50)


class RevenueLending(ModelMixin, models.Model):
    class Meta:
        db_table = 'revenue_lending'
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fico_score = models.CharField(max_length=50)
    equifax_score = models.CharField(max_length=50)
    transunion_score = models.CharField(max_length=50)
    avg_monthly_revenue = models.CharField(max_length=50)
    abg_daily_balance = models.CharField(max_length=50)
    avg_monthly_ending_balance = models.CharField(max_length=50)
    business_debt = models.CharField(max_length=50)
    liens = models.CharField(max_length=50)
    business_bank_account = models.CharField(max_length=50)
    age = models.IntegerField()
    registered_at = models.DateTimeField(null=True, blank=True)
    lender_name = models.CharField(max_length=50)
    personal_credit_score = models.CharField(max_length=50)
    time_in_business = models.CharField(max_length=50)
    business_revenue = models.CharField(max_length=50)
    term_length = models.CharField(max_length=50)
    apr = models.CharField(max_length=50)
    strategy = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class RevolvingCredit(ModelMixin, models.Model):
    class Meta:
        db_table = 'revolving_credit'
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    terms = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    report_to = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class SbaLoan(ModelMixin, models.Model):
    class Meta:
        db_table = 'sba_loan'
    lender_name = models.CharField(max_length=50)
    personal_credit_score = models.CharField(max_length=50)
    time_in_business = models.CharField(max_length=50)
    business_revenue = models.CharField(max_length=15)
    term_length = models.CharField(max_length=10)
    apr = models.CharField(max_length=10)
    strategy = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class ShortTermLoan(ModelMixin, models.Model):
    class Meta:
        db_table = 'short_term_loan'
    lender_name = models.CharField(max_length=50)
    personal_credit_score = models.CharField(max_length=50)
    time_in_business = models.CharField(max_length=50)
    business_revenue = models.CharField(max_length=15)
    term_length = models.CharField(max_length=10)
    apr = models.CharField(max_length=10)
    strategy = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class BusinessTermLoan(ModelMixin, models.Model):
    class Meta:
        db_table = 'term_loan'
    lender_name = models.CharField(max_length=50)
    personal_credit_score = models.CharField(max_length=50)
    time_in_business = models.CharField(max_length=50)
    business_revenue = models.CharField(max_length=15)
    term_length = models.CharField(max_length=10)
    apr = models.CharField(max_length=10)
    strategy = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class StoreCreditVendorList(ModelMixin, models.Model):
    class Meta:
        db_table = 'store_credit_vendor'
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    terms = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    report_to = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class StarterVendorList(ModelMixin, models.Model):
    class Meta:
        db_table = 'starter_vendor_list'
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    terms = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    report_to = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class TollFreeNumber(ModelMixin, models.Model):
    class Meta:
        db_table = 'toll_free_number'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    toll_free_number_needed = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class WebsiteCreation(ModelMixin, models.Model):
    class Meta:
        db_table = 'website_creation'
    industry_name = models.CharField(max_length=50)
    booking_on_page = models.CharField(max_length=50)
    business_name = models.CharField(max_length=50)
    chat_bot = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    theme = models.CharField(max_length=50)
    pages_needed = models.CharField(max_length=50)
    services = models.CharField(max_length=50)
    domain = models.CharField(max_length=50)
    about_you = models.CharField(max_length=500)
    url = models.CharField(max_length=200)
    domain_owned = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class PersonalCreditCard(ModelMixin, models.Model):
    class Meta:
        db_table = 'personal_credit_card'
    cc_name = models.CharField(max_length=50)
    min_credit_score = models.CharField(max_length=50)
    credit_bureau = models.CharField(max_length=50)
    debt_ratio = models.CharField(max_length=50)
    bankruptcy = models.CharField(max_length=50)
    credit_data = models.CharField(max_length=50)
    apr = models.CharField(max_length=50)
    misc_info = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.cc_name


class BusinessCreditCard(ModelMixin, models.Model):
    class Meta:
        db_table = 'business_credit_card'
    cc_name = models.CharField(max_length=50)
    min_credit_score = models.CharField(max_length=50)
    credit_bureau = models.CharField(max_length=50)
    debt_ratio = models.CharField(max_length=50)
    bankruptcy = models.CharField(max_length=50)
    credit_data = models.CharField(max_length=50)
    apr = models.CharField(max_length=50)
    misc_info = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.cc_name


class PersonalLoan(ModelMixin, models.Model):
    class Meta:
        db_table = 'personal_loan'
    lender_name = models.CharField(max_length=50)
    terms = models.CharField(max_length=50)
    inquiries = models.CharField(max_length=50)
    credit_bureau = models.CharField(max_length=50)
    states = models.CharField(max_length=50)
    credit_score = models.CharField(max_length=50)
    emp_length = models.CharField(max_length=50)
    credit_history = models.CharField(max_length=50)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.lender_name


class RevolvingBusinessCreditVendor(ModelMixin, models.Model):
    class Meta:
        db_table = 'revolving_business_credit'
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    terms = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    report_to = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class PersonalCreditTradeLine(ModelMixin, models.Model):
    class Meta:
        db_table = 'personal_credit_tradeline'
    lender_name = models.CharField(max_length=50)
    hard_check = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    strategy = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)