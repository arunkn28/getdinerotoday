from django.shortcuts import render
from django.views import View


class UpgradeView(View):
    def get(self, request):
        return render(request, "home/upgrade.html")


class FinancingView(View):
    def get(self, request):
        return render(request, 'financing.html')


class BusinessCreditBuildingPlanView(View):
    def get(self, request):
        return ""


class CreditSituationView(View):
    def get(self, request):
        return render(request, "home/creditsituation.html")


class BusinessEntity(View):
    def get(self, request):
        return render(request, 'businessEntity.html')


class EinView(View):
    def get(self, request):
        return render(request, 'ein.html')


class BusinessLicenseView(View):
    def get(self, request):
        return render(request, 'businessLicense.html')


class WebsiteCreationOptionsView(View):
    def get(self, request):
        return render(request, 'websiteCreationOptions.html')


class WebsiteCreationPaidView(View):
    def get(self, request):
        return render(request, 'websiteCreationPaid.html')


class WebsiteCreationView(View):
    def get(self, request):
        return render(request, 'websiteCreation.html')


class FaxNumberOptionsView(View):
    def get(self, request):
        return render(request, 'faxNumberOptions.html')


class FaxNumberPaidView(View):
    def get(self, request):
        return render(request, 'faxNumberPaid.html')


class FaxNumberView(View):
    def get(self, request):
        return render(request, 'faxNumber.html')


class FourElevenListingView(View):
    def get(self, request):
        return render(request, 'FourElevenListing.html')


class ProfessionalEmailAddress(View):
    def get(self, request):
        return render(request, 'professionalEmailAddress.html')


class DomainView(View):
    def get(self, request):
        return render(request, 'domain.html')


class TollFreeNumberOptionsView(View):
    def get(self, request):
        return render(request, 'tollFreeNumberOptions.html')


class TollFreeNumberPaidView(View):
    def get(self, request):
        return render(request, 'tollFreeNumberPaid.html')


class TollFreeNumberView(View):
    def get(self, request):
        return render(request, 'tollFreeNumber.html')


class VirtualAddressView(View):
    def get(self, request):
        return render(request, 'virtualAddress.html')


class BusinessBankAccountView(View):
    def get(self, request):
        return render(request, 'businessBankAccount.html')


class MerchantAccountView(View):
    def get(self, request):
        return render(request, 'merchantAccount.html')


class DunsView(View):
    def get(self, request):
        return render(request, 'duns.html')


class SICView(View):
    def get(self, request):
        return render(request, 'sic.html')


class BusinessGoodStandingView(View):
    def get(self, request):
        return render(request, 'businessGoodStanding.html')


class BusinessBackInGoodStandingView(View):
    def get(self, request):
        return render(request, 'businessBackInGoodStanding.html')


class BusinessCreditStep(View):
    def get(self, request):
        return render(request, 'businessCreditStep.html')


class ExperianView(View):
    def get(self, request):
        return render(request, 'experian.html')


class DunnAndBradView(View):
    def get(self, request):
        return render(request, 'dunnbradstreet.html')


class EquifaxView(View):
    def get(self, request):
        return render(request, 'equifax.html')


class StarterVendorListView(View):
    def get(self, request):
        return render(request, "home/starter_vendor_list.html")


class StoreCreditVendorListView(View):
    def get(self, request):
        return render(request, "home/store_credit_vendor_list.html")


class ResolvingBusinessCreditVendorList(View):
    def get(self, request):
        return ""


class CCNoGaurenteeVendorList(View):
    def get(self, request):
        return ""


class PersonalCreditCardsView(View):
    def get(self, request):
        return render(request, "home/personalcreditcards.html")


class BusinessCreditCardsView(View):
    def get(self, request):
        return render(request, "home/businesscreditcards.html")


class ShortTermLoans(View):
    def get(self, request):
        return render(request, "home/shorttermloan.html")


class BusinessTermLoanView(View):
    def get(self, request):
        return ""


class SmallBusinessAdminLoanView(View):
    def get(self, request):
        return ""


class PersonalLoanView(View):
    def get(self, request):
        return render(request, "home/personalloans.html")


class BusinessLineOfCredit(View):
    def get(self, request):
        return ""


class NoCreditCheckFinancing(View):
    def get(self, request):
        return ""


class InvoiceFactoring(View):
    def get(self, request):
        return "home/invoice_factoring.html"


class InvoiceFinancing(View):
    def get(self, request):
        return "home/invoice_financing.html"


class EquipmentFinancing(View):
    def get(self, request):
        return "home/equipmentfincing.html"


class MarketingYourBusiness(View):
    def get(self, request):
        return ""


class BusinessCreditBuildingCourse(View):
    def get(self, request):
        return ""


class OfferFinancingToCustomer(View):
    def get(self, request):
        return ""


class ApplyingForBusinessLoans(View):
    def get(self, request):
        return "home/applyforloan.html"


class CreditRepairSignUp(View):
    def get(self, request):
        return ""


class CreditPrimaryTradeLines(View):
    def get(self, request):
        return ""


class BusinessCreditRepair(View):
    def get(self, request):
        return "home/businesscreditrepair.html"


class BusinessCreditMonitoringSingUp(View):
    def get(self, request):
        return "home/businesscreditmonitoring.html"


class BusinessCreditCardStrategy(View):
    def get(self, request):
        return "home/businesscreditcardstrategy.html"


class MoneyReferringFriends(View):
    def get(self, request):
        return "home/makeextramoney.html"


class InsuranceProduct(View):
    def get(self, request):
        return "home/insurance.html"
