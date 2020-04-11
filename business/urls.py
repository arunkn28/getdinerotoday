from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url('upgrade', login_required(UpgradeView.as_view(), login_url='/user/login'), name='upgrade'),
    url('financing', login_required(FinancingView.as_view(), login_url='/user/login'), name='financing'),
    url('business-credit-plan', login_required(BusinessCreditBuildingPlanView.as_view(), login_url='/user/login'),
        name='business-credit-plan'),
    url('credit-situation', login_required(CreditSituationView.as_view(), login_url='/user/login'),
        name='credit-situation'),
    url('business-entity', login_required(BusinessEntity.as_view(), login_url='/user/login'),
        name='business-entity'),
    url('ein', login_required(EinView.as_view(), login_url='/user/login'),
        name='ein'),
    url('business-license', login_required(BusinessLicenseView.as_view(), login_url='/user/login'),
        name='business-license'),
    url('website-creation', login_required(WebsiteCreationView.as_view(), login_url='/user/login'),
        name='website-creation'),
    url('fax-number', login_required(FaxNumberView.as_view(), login_url='/user/login'),
        name='fax-number'),
    url('four-eleven', login_required(FourElevenListing.as_view(), login_url='/user/login'),
        name='four-eleven'),
    url('professional-email', login_required(ProfessionalEmailAddress.as_view(), login_url='/user/login'),
        name='professional-email'),
    url('domain', login_required(DomainView.as_view(), login_url='/user/login'),
        name='domain'),
    url('toll-free', login_required(TollFreeNumberView.as_view(), login_url='/user/login'),
        name='toll-free'),
    url('virtual-address', login_required(VirtualAddressView.as_view(), login_url='/user/login'),
        name='virtual-address'),
    url('business-bank-account', login_required(BusinessBankAccountView.as_view(), login_url='/user/login'),
        name='business-bank-account'),
    url('merchant-account', login_required(MerchantAccountView.as_view(), login_url='/user/login'),
        name='merchant-account'),
    url('duns', login_required(DunsView.as_view(), login_url='/user/login'), name='duns'),
    url('sic', login_required(SICView.as_view(), login_url='/user/login'), name='sic'),
    url('business-good-standing', login_required(BusinessGoodStandingView.as_view(), login_url='/user/login'),
        name='business-good-standing'),
    url('business-in-good-standing', login_required(BusinessBackInGoodStandingView.as_view(), login_url='/user/login'),
        name='business-in-good-standing'),
    url('business-credit-step', login_required(BusinessCreditStep.as_view(), login_url='/user/login'),
        name='business-credit-step'),
    url('experian', login_required(ExperianView.as_view(), login_url='/user/login'),
        name='experian'),
    url('dunn-brad', login_required(DunnAndBradView.as_view(), login_url='/user/login'),
        name='dunn-brad'),
    url('equifax', login_required(EquifaxView.as_view(), login_url='/user/login'),
        name='equifax'),
    url('vendor-list', login_required(StarterVendorListView.as_view(), login_url='/user/login'),
        name='vendor-list'),
    url('store-credit-vendor-list', login_required(StoreCreditVendorListView.as_view(), login_url='/user/login'),
        name='store-credit-vendor-list'),
    url('business-credit-vendor', login_required(ResolvingBusinessCreditVendorList.as_view(), login_url='/user/login'),
        name='business-credit-vendor'),
    url('cc-credit-vendor', login_required(CCNoGaurenteeVendorList.as_view(), login_url='/user/login'),
        name='cc-credit-vendor'),
    url('personal-credit-card', login_required(PersonalCreditCardsView.as_view(), login_url='/user/login'),
        name='personal-credit-card'),
    url('business-credit-card', login_required(BusinessCreditCardsView.as_view(), login_url='/user/login'),
        name='business-credit-card'),
    url('short-term-loan', login_required(ShortTermLoans.as_view(), login_url='/user/login'),
        name='short-term-loan'),
    url('business-term-loan', login_required(BusinessTermLoanView.as_view(), login_url='/user/login'),
        name='business-term-loan'),
    url('small-business-loan', login_required(SmallBusinessAdminLoanView.as_view(), login_url='/user/login'),
        name='small-business-loan'),
    url('personal-loan', login_required(PersonalLoanView.as_view(), login_url='/user/login'),
        name='personal-loan'),
    url('business-line-credit', login_required(BusinessLineOfCredit.as_view(), login_url='/user/login'),
        name='business-line-credit'),
    url('nocredit-financing', login_required(NoCreditCheckFinancing.as_view(), login_url='/user/login'),
        name='nocredit-financing'),
    url('invoice-factoring', login_required(InvoiceFactoring.as_view(), login_url='/user/login'),
        name='invoice-factoring'),
    url('invoice-financing', login_required(InvoiceFinancing.as_view(), login_url='/user/login'),
        name='invoice-financing'),
    url('invoice-financing', login_required(InvoiceFinancing.as_view(), login_url='/user/login'),
        name='invoice-financing'),
    url('equipment-financing', login_required(EquipmentFinancing.as_view(), login_url='/user/login'),
        name='equipment-financing'),
    url('marketing-business', login_required(MarketingYourBusiness.as_view(), login_url='/user/login'),
        name='marketing-business'),
    url('business-credit-course', login_required(BusinessCreditBuildingCourse.as_view(), login_url='/user/login'),
        name='business-credit-course'),
    url('customer-financing', login_required(OfferFinancingToCustomer.as_view(), login_url='/user/login'),
        name='customer-financing'),
    url('apply-business-loans', login_required(ApplyingForBusinessLoans.as_view(), login_url='/user/login'),
        name='apply-business-loans'),
    url('credit-repair', login_required(CreditRepairSignUp.as_view(), login_url='/user/login'),
        name='credit-repair'),
    url('credit-trade-lines', login_required(CreditPrimaryTradeLines.as_view(), login_url='/user/login'),
        name='credit-trade-lines'),
    url('business-credit-repair', login_required(BusinessCreditRepair.as_view(), login_url='/user/login'),
        name='business-credit-repair'),
    url('business-credit-monitoring', login_required(BusinessCreditMonitoringSingUp.as_view(), login_url='/user/login'),
        name='business-credit-monitoring'),
    url('business-credit-strategy', login_required(BusinessCreditCardStrategy.as_view(), login_url='/user/login'),
        name='business-credit-strategy'),
    url('refer', login_required(MoneyReferringFriends.as_view(), login_url='/user/login'),
        name='refer'),
    url('insurance-products', login_required(InsuranceProduct.as_view(), login_url='/user/login'),
        name='insurance-products'),
]