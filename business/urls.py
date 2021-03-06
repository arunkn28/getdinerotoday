from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'business'
urlpatterns = [
    url('upgrade/', login_required(UpgradeView.as_view(), login_url='/user/login'), name='upgrade'),
    url('financing/', login_required(FinancingView.as_view(), login_url='/user/login'), name='financing'),
    url('financing-plan-1/', login_required(FinancingPlan1View.as_view(), login_url='/user/login'), name='financing_plan_1'),
    url('financing-plan-2/', login_required(FinancingPlan2View.as_view(), login_url='/user/login'), name='financing_plan_2'),
    url('financing-plan-3/', login_required(FinancingPlan3View.as_view(), login_url='/user/login'), name='financing_plan_3'),
    url('financing-plan-6/', login_required(FinancingPlan6View.as_view(), login_url='/user/login'), name='financing_plan_6'),
    url('financing-plan-7/', login_required(FinancingPlan7View.as_view(), login_url='/user/login'), name='financing_plan_7'),
    url('financing-plan-8/', login_required(FinancingPlan8View.as_view(), login_url='/user/login'), name='financing_plan_8'),
    url('financing-plan-10/', login_required(FinancingPlan10View.as_view(), login_url='/user/login'), name='financing_plan_10'),
    url('financing-plan-12/', login_required(FinancingPlan12View.as_view(), login_url='/user/login'), name='financing_plan_12'),
    url('financing-plan-15/', login_required(FinancingPlan15View.as_view(), login_url='/user/login'), name='financing_plan_15'),
    url('business-credit-plan/', login_required(BusinessCreditBuildingPlanView.as_view(), login_url='/user/login'),
        name='business-credit-plan'),
    url('business-plan-1/', login_required(BusinessPlan1View.as_view(), login_url='/user/login'), name='business_plan_1'),
    url('business-plan-2/', login_required(BusinessPlan2View.as_view(), login_url='/user/login'), name='business_plan_2'),
    url('business-plan-3/', login_required(BusinessPlan3View.as_view(), login_url='/user/login'), name='business_plan_3'),
    url('credit-situation/', login_required(CreditSituationView.as_view(), login_url='/user/login'),
        name='credit-situation'),
    url('business-entity/', login_required(BusinessEntity.as_view(), login_url='/user/login'),
        name='business-entity'),
    url('ein/', login_required(EinView.as_view(), login_url='/user/login'),
        name='ein'),
    url('business-license/', login_required(BusinessLicenseView.as_view(), login_url='/user/login'),
        name='business-license'),
    url('website-creation-options', login_required(WebsiteCreationOptionsView.as_view(), login_url='/user/login'),
        name='website-creation-options'),
    url('website-creation-paid', login_required(WebsiteCreationPaidView.as_view(), login_url='/user/login'),
        name='website-creation-paid'),
    url('website-creation/', login_required(WebsiteCreationView.as_view(), login_url='/user/login'),
        name='website-creation'),
    url('fax-number-options', login_required(FaxNumberOptionsView.as_view(), login_url='/user/login'),
        name='fax-number-options'),
    url('fax-number-paid', login_required(FaxNumberPaidView.as_view(), login_url='/user/login'),
        name='fax-number-paid'),
    url('fax-number/', login_required(FaxNumberView.as_view(), login_url='/user/login'),
        name='fax-number'),
    url('four-eleven/', login_required(FourElevenListingView.as_view(), login_url='/user/login'),
        name='four-eleven'),
    url('professional-email/', login_required(ProfessionalEmailAddress.as_view(), login_url='/user/login'),
        name='professional-email'),
    url('domain/', login_required(DomainView.as_view(), login_url='/user/login'),
        name='domain'),
    url('toll-free-options/', login_required(TollFreeNumberOptionsView.as_view(), login_url='/user/login'),
        name='toll-free-options'),
    url('toll-free-paid/', login_required(TollFreeNumberPaidView.as_view(), login_url='/user/login'),
        name='toll-free-paid'),
    url('toll-free/', login_required(TollFreeNumberView.as_view(), login_url='/user/login'),
        name='toll-free'),
    url('virtual-address/', login_required(VirtualAddressView.as_view(), login_url='/user/login'),
        name='virtual-address'),
    url('business-bank-account/', login_required(BusinessBankAccountView.as_view(), login_url='/user/login'),
        name='business-bank-account'),
    url('merchant-account/', login_required(MerchantAccountView.as_view(), login_url='/user/login'),
        name='merchant-account'),
    url('duns/', login_required(DunsView.as_view(), login_url='/user/login'), name='duns'),
    url('sic/', login_required(SICView.as_view(), login_url='/user/login'), name='sic'),
    url('business-good-standing/', login_required(BusinessGoodStandingView.as_view(), login_url='/user/login'),
        name='business-good-standing'),
    url('business-in-good-standing/', login_required(BusinessBackInGoodStandingView.as_view(), login_url='/user/login'),
        name='business-in-good-standing'),
    url('business-credit-step/', login_required(BusinessCreditStep.as_view(), login_url='/user/login'),
        name='business-credit-step'),
    url('experian/', login_required(ExperianView.as_view(), login_url='/user/login'),
        name='experian'),
    url('dunn-brad/', login_required(DunnAndBradView.as_view(), login_url='/user/login'),
        name='dunn-brad'),
    url('equifax/', login_required(EquifaxView.as_view(), login_url='/user/login'),
        name='equifax'),
    url('store-credit-vendor-list/', login_required(StoreCreditVendorListView.as_view(), login_url='/user/login'),
        name='store-credit-vendor-list'),
    url('vendor-list/', login_required(StarterVendorListView.as_view(), login_url='/user/login'),
        name='vendor-list'),
    url('lender-detail/(\d+)/', login_required(LeaderDetailsView.as_view(), login_url='/user/login'),
        name='lender_detail'),
    url('business-credit-vendor/', login_required(RevolvingBusinessCreditVendorList.as_view(), login_url='/user/login'),
        name='business-credit-vendor'),
    url('revolving-credit-details/(\d+)/', login_required(RevolvingDetailsView.as_view(), login_url='/user/login'),
        name='revolving-credit-details'),
    url('cc-credit-vendor/', login_required(CCNoGuaranteeVendorList.as_view(), login_url='/user/login'),
        name='cc-credit-vendor'),
    url('nopg-detail/(\d+)/', login_required(NoPgDetailsView.as_view(), login_url='/user/login'),
        name='nopg-detail'),


    url('personal-credit-card/', login_required(PersonalCreditCardsView.as_view(), login_url='/user/login'),
        name='personal-credit-card'),
    url('business-credit-card/', login_required(BusinessCreditCardsView.as_view(), login_url='/user/login'),
        name='business-credit-card'),
    url('short-term-loan/', login_required(ShortTermLoans.as_view(), login_url='/user/login'),
        name='short-term-loan'),
    url('business-term-loan/', login_required(BusinessTermLoanView.as_view(), login_url='/user/login'),
        name='business-term-loan'),
    url('small-business-loan/', login_required(SmallBusinessAdminLoanView.as_view(), login_url='/user/login'),
        name='small-business-loan'),
    url('personal-loan/', login_required(PersonalLoanView.as_view(), login_url='/user/login'),
        name='personal-loan'),
    url('business-line-credit/', login_required(BusinessLineOfCredit.as_view(), login_url='/user/login'),
        name='business-line-credit'),
    url('nocredit-financings/', login_required(NoCreditCheckFinancing.as_view(), login_url='/user/login'),
        name='nocredit-financings'),
    url('invoice-factoring/', login_required(InvoiceFactoring.as_view(), login_url='/user/login'),
        name='invoice-factoring'),
    url('invoice-financings/', login_required(InvoiceFinancing.as_view(), login_url='/user/login'),
        name='invoice-financings'),
    url('equipment-financings/', login_required(EquipmentFinancingView.as_view(), login_url='/user/login'),
        name='equipment-financings'),
    url('apply-loan/', login_required(EquipmentFinancingView.as_view(), login_url='/user/login'),
        name='applyforloan'),
    url('marketing-business/', login_required(MarketingYourBusiness.as_view(), login_url='/user/login'),
        name='marketing-business'),
    url('customer-financing-offer/', login_required(OfferFinancingToCustomer.as_view(), login_url='/user/login'),
        name='customer-financing-offer'),
    url('apply-loans', login_required(ApplyingForLoans.as_view(), login_url='/user/login'),
        name='apply-loans'),
    url('credit-repair-options/', login_required(CreditRepairOptionsView.as_view(), login_url='/user/login'),
        name='credit-repair-options'),
    url('credit-repair-paid/', login_required(CreditRepairPaidView.as_view(), login_url='/user/login'),
        name='credit-repair-paid'),
    url('credit-repair/', login_required(CreditRepairView.as_view(), login_url='/user/login'),
        name='credit-repair'),
    url('credit-trade-lines/', login_required(CreditPrimaryTradeLines.as_view(), login_url='/user/login'),
        name='credit-trade-lines'),
    url('business-credit-repair-new/', login_required(BusinessCreditRepair.as_view(), login_url='/user/login'),
        name='business-credit-repair-new'),
    url('business-credit-monitoring/', login_required(BusinessCreditMonitoringSingUp.as_view(), login_url='/user/login'),
        name='business-credit-monitoring'),
    url('business-credit-strategy/', login_required(BusinessCreditCardStrategy.as_view(), login_url='/user/login'),
        name='business-credit-strategy'),
    url('refer/', login_required(MoneyReferringFriends.as_view(), login_url='/user/login'),
        name='refer'),
    url('insurance-products/', login_required(InsuranceProduct.as_view(), login_url='/user/login'),
        name='insurance-products'),
    url('credit-repair-1/', login_required(CreditRepairPlan1View.as_view(), login_url='/user/login'), name='credit_repair_1'),
    url('credit-repair-2/', login_required(CreditRepairPlan2View.as_view(), login_url='/user/login'), name='credit_repair_2'),
    url('credit-repair-3/', login_required(CreditRepairPlan3View.as_view(), login_url='/user/login'), name='credit_repair_3'),
    url('credit-repair-4/', login_required(CreditRepairPlan4View.as_view(), login_url='/user/login'), name='credit_repair_4'),
    url('credit-repair-5/', login_required(CreditRepairPlan5View.as_view(), login_url='/user/login'), name='credit_repair_5'),
    url('credit-repair-6/', login_required(CreditRepairPlan6View.as_view(), login_url='/user/login'), name='credit_repair_6'),
    url('credit-repair-7/', login_required(CreditRepairPlan7View.as_view(), login_url='/user/login'), name='credit_repair_7'),
    url('credit-repair-8/', login_required(CreditRepairPlan8View.as_view(), login_url='/user/login'), name='credit_repair_8'),
    url('credit-repair-9/', login_required(CreditRepairPlan9View.as_view(), login_url='/user/login'), name='credit_repair_9'),
    url('credit-repair-10/', login_required(CreditRepairPlan10View.as_view(), login_url='/user/login'), name='credit_repair_10'),
    url('credit-repair-11/', login_required(CreditRepairPlan11View.as_view(), login_url='/user/login'), name='credit_repair_11'),
    url('credit-repair-12/', login_required(CreditRepairPlan12View.as_view(), login_url='/user/login'), name='credit_repair_12'),
    url('credit-repair-13/', login_required(CreditRepairPlan13View.as_view(), login_url='/user/login'), name='credit_repair_13'),
    url('credit-repair-14/', login_required(CreditRepairPlan14View.as_view(), login_url='/user/login'), name='credit_repair_14'),
    url('credit-repair-15/', login_required(CreditRepairPlan15View.as_view(), login_url='/user/login'), name='credit_repair_15'),
    url('credit-repair-16/', login_required(CreditRepairPlan16View.as_view(), login_url='/user/login'), name='credit_repair_16'),
    url('credit-repair-17/', login_required(CreditRepairPlan17View.as_view(), login_url='/user/login'), name='credit_repair_17'),
]
