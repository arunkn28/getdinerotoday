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
        data=[
            {"Name":"Enco Manufacturing Company","category":'',"reportTo":'Dun &amp; Bradstreet',"link":"1"},
            {"Name":"REW Materials","category":'',"reportTo":'Equifax Small Business',"link":"2"},
            {"Name":"United Rentals","category":'',"reportTo":'Dun &amp; Bradstreet',"link":"3"},
            {"Name":"Copperfield","category":'',"reportTo":'Equifax Small Business',"link":"4"},
        ]
        return render(request, 'starter_vendor_list.html',{"list_data":data})


class StoreCreditVendorListView(View):
    def get(self, request):
        return render(request, "home/store_credit_vendor_list.html")


class ResolvingBusinessCreditVendorList(View):
    def get(self, request):
        data=[
            {"Name":"Enco Manufacturing Company","category":'',"reportTo":'Dun &amp; Bradstreet',"link":"1"},
            {"Name":"REW Materials","category":'',"reportTo":'Equifax Small Business',"link":"2"},
            {"Name":"United Rentals","category":'',"reportTo":'Dun &amp; Bradstreet',"link":"3"},
            {"Name":"Copperfield","category":'',"reportTo":'Equifax Small Business',"link":"4"},
        ]
        return render(request, 'store_credit_vendor_list.html',{"list_data":data})

class leaderDetailsView(View):
    def get(self, request,state):
        data={
            "name":"Fleet-One Local Fleet Card",
            "category":'',
            "reportTo":'Dun &amp; Bradstreet, Experian Business and Equifax Small Business',
            "terms":'',
            "description":' If your business uses cars, vans or trucks, Fleet-One Local Fuel Cards can make your job easier with security, control, convenience and savings. Use the Fleet-One Local card to pay for fuel and maintenance. With reduced fraud and more control, the savings for your business add up. Approval Requirements: Do not apply for this no personal guarantor account until you have at least 10 reporting trade lines and one trade line with a $10k credit limit reporting. They will check 411 listing, secretary of state for status of your corporation or LLC to make sure it&#39;s in good standing. You&#39;ll need to supply your EIN, copy of a voided business check, copy of a utility bill showing the business address and phone number, and a copy of your business license. (if a business license is required in your state) Leave the personal guarantor section blank.'
            }
        return render(request, 'lender_detail.html',data)




class RevolvingBusinessCreditVendorList(View):
    def get(self, request):
        data=[
            {"Name":"Enco Manufacturing Company","category":'',"reportTo":'Dun &amp; Bradstreet',"link":"1"},
            {"Name":"REW Materials","category":'',"reportTo":'Equifax Small Business',"link":"2"},
            {"Name":"United Rentals","category":'',"reportTo":'Dun &amp; Bradstreet',"link":"3"},
            {"Name":"Copperfield","category":'',"reportTo":'Equifax Small Business',"link":"4"},
        ]
        return render(request, 'revolving.html',{"list_data":data})

class revolvingDetailsView(View):
    def get(self, request,state):
        data={
            "name":"Fleet-One Local Fleet Card",
            "category":'',
            "reportTo":'Dun &amp; Bradstreet, Experian Business and Equifax Small Business',
            "terms":'',
            "description":' If your business uses cars, vans or trucks, Fleet-One Local Fuel Cards can make your job easier with security, control, convenience and savings. Use the Fleet-One Local card to pay for fuel and maintenance. With reduced fraud and more control, the savings for your business add up. Approval Requirements: Do not apply for this no personal guarantor account until you have at least 10 reporting trade lines and one trade line with a $10k credit limit reporting. They will check 411 listing, secretary of state for status of your corporation or LLC to make sure it&#39;s in good standing. You&#39;ll need to supply your EIN, copy of a voided business check, copy of a utility bill showing the business address and phone number, and a copy of your business license. (if a business license is required in your state) Leave the personal guarantor section blank.'
            }
        return render(request, 'revolving_credit_detail.html',data)

class CCNoGaurenteeVendorList(View):
    def get(self, request):
        data=[
            {"Name":"Enco Manufacturing Company","category":'',"reportTo":'Dun &amp; Bradstreet',"link":"1"},
            {"Name":"REW Materials","category":'',"reportTo":'Equifax Small Business',"link":"2"},
            {"Name":"United Rentals","category":'',"reportTo":'Dun &amp; Bradstreet',"link":"3"},
            {"Name":"Copperfield","category":'',"reportTo":'Equifax Small Business',"link":"4"},
        ]
        return render(request, 'nopg.html',{"list_data":data})


class noPgDetailsView(View):
    def get(self, request,state):
        data={
            "name":"Fleet-One Local Fleet Card",
            "category":'',
            "reportTo":'Dun &amp; Bradstreet, Experian Business and Equifax Small Business',
            "terms":'',
            "description":' If your business uses cars, vans or trucks, Fleet-One Local Fuel Cards can make your job easier with security, control, convenience and savings. Use the Fleet-One Local card to pay for fuel and maintenance. With reduced fraud and more control, the savings for your business add up. Approval Requirements: Do not apply for this no personal guarantor account until you have at least 10 reporting trade lines and one trade line with a $10k credit limit reporting. They will check 411 listing, secretary of state for status of your corporation or LLC to make sure it&#39;s in good standing. You&#39;ll need to supply your EIN, copy of a voided business check, copy of a utility bill showing the business address and phone number, and a copy of your business license. (if a business license is required in your state) Leave the personal guarantor section blank.'
            }
        return render(request, 'nopg_detail.html',data)



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
        return render(request, "home/invoice_factoring.html")


class InvoiceFinancing(View):
    def get(self, request):
        return render(request, "home/invoice_financing.html")


class EquipmentFinancing(View):
    def get(self, request):
        return render(request, "home/equipmentfincing.html")










class MarketingYourBusiness(View):
    def get(self, request):
        return render(request, 'marketingYourBusiness.html')

class OfferFinancingToCustomer(View):
    def get(self, request):
        return render(request, 'customerFinancing.html')

class ApplyingForBusinessLoans(View):
    def get(self, request):
        return render(request, 'applyforLoan.html')


class CreditRepairOptionsView(View):
    def get(self, request):
        return render(request, 'creditRepairOptions.html')

class CreditRepairPaidView(View):
    def get(self, request):
        return render(request, 'creditRepairPaid.html')

class CreditRepairView(View):
    def get(self, request):
        return render(request, 'creditRepair.html')

class CreditPrimaryTradeLines(View):
    def get(self, request):
        return render(request, 'creditPrimaryTradeline.html')


class BusinessCreditRepair(View):
    def get(self, request):
        return render(request, 'businessCreditRepair.html')

class BusinessCreditMonitoringSingUp(View):
    def get(self, request):
        return render(request, 'businessCreditMonitoringSingup.html')


class BusinessCreditCardStrategy(View):
    def get(self, request):
        return render(request, 'businessCreditCardStrategy.html')


class MoneyReferringFriends(View):
    def get(self, request):
        return render(request, 'MoneyReferringFriends.html')


class InsuranceProduct(View):
    def get(self, request):
        return render(request, 'insuranceProduct.html')



