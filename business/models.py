from django.db import models
from user.models import Profile


# Create your models here.
class Domain(models.Model):
    class Meta:
        db_table = 'domain'
    user = models.ForeignKey(Profile,  on_delete=models.CASCADE)
    domain_name = models.CharField(max_length=50)
    domain_needed = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class EquipmentFinancing(models.Model):
    class Meta:
        db_table = 'equipment_financing'
    lender_name = models.CharField(max_length=50)
    personal_credit_score = models.CharField(max_length=50)
    time_in_business = models.CharField(max_length=50)
    business_revenue = models.CharField(max_length=15)
    term_length = models.CharField(max_length=10)
    apr = models.CharField(max_length=10)
    strategy = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Fax(models.Model):
    class Meta:
        db_table = 'fax'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fax_needed = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50)
    updated_at = models.DateTimeField()


class InvoiceFactoring(models.Model):
    class Meta:
        db_table = 'invoice_factoring'
    lender_name = models.CharField(max_length=50)
    personal_credit_score = models.CharField(max_length=50)
    time_in_business = models.CharField(max_length=50)
    business_revenue = models.CharField(max_length=15)
    term_length = models.CharField(max_length=10)
    apr = models.CharField(max_length=10)
    strategy = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class InvoiceFinancing(models.Model):
    class Meta:
        db_table = 'invoice_financing'

    lender_name = models.CharField(max_length=50)
    personal_credit_score = models.CharField(max_length=50)
    time_in_business = models.CharField(max_length=50)
    business_revenue = models.CharField(max_length=15)
    term_length = models.CharField(max_length=10)
    apr = models.CharField(max_length=10)
    strategy = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Category(models.Model):
    class Meta:
        db_table = 'category'
    title = models.CharField(max_length=50)


class Lender(models.Model):
    class Meta:
        db_table = 'lender'
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    report_to = models.CharField(max_length=50)
    monthly_payment = models.CharField(max_length=15)
    estimated_term = models.CharField(max_length=50)
    payment_terms = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class LinesOfCredit(models.Model):
    class Meta:
        db_table = 'lines_of_credit'

    lender_name = models.CharField(max_length=50)
    personal_credit_score = models.CharField(max_length=50)
    time_in_business = models.CharField(max_length=50)
    business_revenue = models.CharField(max_length=15)
    term_length = models.CharField(max_length=10)
    apr = models.CharField(max_length=10)
    strategy = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Nopg(models.Model):
    class Meta:
        db_table = 'nopg'
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    report_to = models.CharField(max_length=50)
    monthly_payment = models.CharField(max_length=15)
    estimated_term = models.DateField()
    payment_terms = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class ProfessionalEmailAddress(models.Model):
    class Meta:
        db_table = 'professional_email_address'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    email_address_needed = models.CharField(max_length=50)
    domain_present = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Progress(models.Model):
    class Meta:
        db_table = 'progress'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    website_creation = models.CharField(max_length=50)
    dns_number = models.CharField(max_length=50)
    website_creation = models.CharField(max_length=50)
    virtual_number = models.CharField(max_length=50)
    fax_number = models.CharField(max_length=50)
    toll_free_number = models.CharField(max_length=50)
    business_bank_account = models.CharField(max_length=50)
    listing = models.CharField(max_length=50)
    professional_email_address = models.CharField(max_length=50)
    domain = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Industry(models.Model):
    class Meta:
        db_table = 'industry'
    title = models.CharField(max_length=50)


class RevenueLending(models.Model):
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
    registerd_at = models.DateTimeField()
    lender_name = models.CharField(max_length=50)
    personal_credit_score = models.CharField(max_length=50)
    time_in_business = models.CharField(max_length=50)
    business_revenue = models.CharField(max_length=50)
    term_length = models.CharField(max_length=50)
    apr = models.CharField(max_length=50)
    strategy = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class RevolvingCredit(models.Model):
    class Meta:
        db_table = 'revolving_credit'
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    terms = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    report_to = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class SbaLoan(models.Model):
    class Meta:
        db_table = 'sba_loan'
    lender_name = models.CharField(max_length=50)
    personal_credit_score = models.CharField(max_length=50)
    time_in_business = models.CharField(max_length=50)
    business_revenue = models.CharField(max_length=15)
    term_length = models.CharField(max_length=10)
    apr = models.CharField(max_length=10)
    strategy = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class ShortTermLoan(models.Model):
    class Meta:
        db_table = 'short_term_loan'
    lender_name = models.CharField(max_length=50)
    personal_credit_score = models.CharField(max_length=50)
    time_in_business = models.CharField(max_length=50)
    business_revenue = models.CharField(max_length=15)
    term_length = models.CharField(max_length=10)
    apr = models.CharField(max_length=10)
    strategy = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class TermLoan(models.Model):
    class Meta:
        db_table = 'term_loan'
    lender_name = models.CharField(max_length=50)
    personal_credit_score = models.CharField(max_length=50)
    time_in_business = models.CharField(max_length=50)
    business_revenue = models.CharField(max_length=15)
    term_length = models.CharField(max_length=10)
    apr = models.CharField(max_length=10)
    strategy = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class StoreCreditVendorList(models.Model):
    class Meta:
        db_table = 'store_credit_vendor'
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    terms = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    report_to = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class TollFreeNumber(models.Model):
    class Meta:
        db_table = 'toll_free_number'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    toll_free_number_needed = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class WebsiteCreation(models.Model):
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
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()