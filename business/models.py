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
    estimated_term = models.DateField()
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




