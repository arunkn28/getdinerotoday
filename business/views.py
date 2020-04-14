from django.shortcuts import render
from .models import (
    Profile, Lender, StoreCreditVendorList, RevolvingCredit, Nopg, ShortTermLoan, BusinessTermLoan, SbaLoan,
    LinesOfCredit, StarterVendorList
)
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse


def get_business_plan_context():
    lenders = Lender.objects.all()
    store_credits = StoreCreditVendorList.objects.all()
    revolvings = RevolvingCredit.objects.all()
    nopgs = Nopg.objects.all()
    context = {
        "lenders": lenders,
        "store_credits": store_credits,
        "revolvings": revolvings,
        "nopgs": nopgs
    }

    return context


class BusinessPlan1View(View):
    def get(self, request):
        return render(request, "home/businessplan1.html", context=get_business_plan_context())


class BusinessPlan2View(View):
    def get(self, request):
        return render(request, "home/businessplan2.html", context=get_business_plan_context())


class BusinessPlan3View(View):
    def get(self, request):
        return render(request, "home/businessplan3.html", context=get_business_plan_context())


class BusinessCreditBuildingPlanView(View):
    def get(self, request):
        return render(request, "home/business.html")

    def post(self, request):
        data = request.POST
        business_time = int(data['business_time'])
        trade_lines = int(data['trade_lines'])
        if business_time == 1:
            if trade_lines == 1:
                return HttpResponseRedirect(reverse("business:business_plan_1"))
            elif trade_lines == 2:
                return HttpResponseRedirect(reverse("business:business_plan_2"))
            elif trade_lines == 3:
                return HttpResponseRedirect(reverse("business:business_plan_3"))
        elif business_time == 2:
            if trade_lines == 1:
                return HttpResponseRedirect(reverse("business:business_plan_1"))
            elif trade_lines == 2:
                return HttpResponseRedirect(reverse("business:business_plan_2"))
            elif trade_lines == 3:
                return HttpResponseRedirect(reverse("business:business_plan_3"))
        elif business_time == 3:
            if trade_lines == 1:
                return HttpResponseRedirect(reverse("business:business_plan_1"))
            elif trade_lines == 2:
                return HttpResponseRedirect(reverse("business:business_plan_2"))
            elif trade_lines == 3:
                return HttpResponseRedirect(reverse("business:business_plan_3"))


class UpgradeView(View):
    def get(self, request):
        return render(request, "home/upgrade.html")


class FinancingView(View):
    def get(self, request):
        return render(request, 'financing.html')


class CreditSituationView(View):
    def get(self, request):
        return render(request, "home/creditsituation.html")


class BusinessEntity(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/businessEntity.html')


class EinView(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/ein.html')


class BusinessLicenseView(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/businessLicense.html')


class WebsiteCreationOptionsView(View):
    def get(self, request):
        profile = Profile.objects.filter(user=request.user)
        website_creation_paid = False
        if profile:
            website_creation_paid = profile[0].website_creation_paid
        if website_creation_paid:
            return redirect(reverse('business:website-creation-paid'))
        return redirect(reverse('business:website-creation'))
        # return render(request, 'businessCreditBuilding/websiteCreationOptions.html', {'website_creation_paid': website
        # _creation_paid})


class WebsiteCreationPaidView(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/websiteCreationPaid.html')


class WebsiteCreationView(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/websiteCreation.html')


class FaxNumberOptionsView(View):
    def get(self, request):
        profile = Profile.objects.filter(user=request.user)
        fax_number_paid = False
        if profile:
            fax_number_paid = profile[0].fax_number_paid
        if fax_number_paid:
            return redirect(reverse('business:fax-number-paid'))
        return redirect(reverse('business:fax-number'))
        # return render(request, 'businessCreditBuilding/faxNumberOptions.html', {'fax_number_paid': fax_number_paid})


class FaxNumberPaidView(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/faxNumberPaid.html')


class FaxNumberView(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/faxNumber.html')


class FourElevenListingView(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/FourElevenListing.html')


class ProfessionalEmailAddress(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/professionalEmailAddress.html')


class DomainView(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/domain.html')


class TollFreeNumberOptionsView(View):
    def get(self, request):
        profile = Profile.objects.filter(user=request.user)
        toll_free_number_paid = False
        if profile:
            toll_free_number_paid = profile[0].toll_free_number_paid
        if toll_free_number_paid:
            return redirect(reverse('business:toll-free-paid'))
        return redirect(reverse('business:toll-free'))
        # return render(request, 'businessCreditBuilding/tollFreeNumberOptions.html', {'toll_free_number_paid':
        # toll_free_number_paid})


class TollFreeNumberPaidView(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/tollFreeNumberPaid.html')


class TollFreeNumberView(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/tollFreeNumber.html')


class VirtualAddressView(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/virtualAddress.html')


class BusinessBankAccountView(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/businessBankAccount.html')


class MerchantAccountView(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/merchantAccount.html')


class DunsView(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/duns.html')


class SICView(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/sic.html')


class BusinessGoodStandingView(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/businessGoodStanding.html')


class BusinessBackInGoodStandingView(View):
    def get(self, request):
        return render(request, 'businessCreditBuilding/businessBackInGoodStanding.html')


class BusinessCreditStep(View):
    def get(self, request):
        return render(request, 'businessCreditStep.html')


class ExperianView(View):
    def get(self, request):
        return render(request, 'creditBureaus/experian.html')


class DunnAndBradView(View):
    def get(self, request):
        return render(request, 'creditBureaus/dunnbradstreet.html')


class EquifaxView(View):
    def get(self, request):
        return render(request, 'creditBureaus/equifax.html')


class StarterVendorListView(View):
    def get(self, request):
        starter_vendors = StarterVendorList.objects.all()
        return render(request, 'cooperateCredit/starter_vendor_list.html', {"starter_vendors": starter_vendors})


class StoreCreditVendorListView(View):
    def get(self, request):
        store_credit_vendors = StoreCreditVendorList.objects.all()
        return render(request, "cooperateCredit/store_credit_vendor_list.html",
                      {"store_credit_vendors": store_credit_vendors})


class ResolvingBusinessCreditVendorList(View):
    def get(self, request):
        data = [
            {"Name": "Enco Manufacturing Company", "category": '', "reportTo": 'Dun &amp; Bradstreet', "link": "1"},
            {"Name": "REW Materials", "category": '', "reportTo": 'Equifax Small Business', "link": "2"},
            {"Name": "United Rentals", "category": '', "reportTo": 'Dun &amp; Bradstreet', "link": "3"},
            {"Name": "Copperfield", "category": '', "reportTo": 'Equifax Small Business', "link": "4"},
        ]
        return render(request, 'cooperateCredit/store_credit_vendor_list.html', {"list_data": data})


class LeaderDetailsView(View):
    def get(self, request, state):
        data = {
            "name": "Fleet-One Local Fleet Card",
            "category": '',
            "reportTo": 'Dun &amp; Bradstreet, Experian Business and Equifax Small Business',
            "terms": '',
            "description": ' If your business uses cars, vans or trucks, Fleet-One Local Fuel Cards can make your job easier with security, control, convenience and savings. Use the Fleet-One Local card to pay for fuel and maintenance. With reduced fraud and more control, the savings for your business add up. Approval Requirements: Do not apply for this no personal guarantor account until you have at least 10 reporting trade lines and one trade line with a $10k credit limit reporting. They will check 411 listing, secretary of state for status of your corporation or LLC to make sure it&#39;s in good standing. You&#39;ll need to supply your EIN, copy of a voided business check, copy of a utility bill showing the business address and phone number, and a copy of your business license. (if a business license is required in your state) Leave the personal guarantor section blank.'
        }
        return render(request, 'cooperateCredit/lender_detail.html', data)


class RevolvingBusinessCreditVendorList(View):
    def get(self, request):
        data = [
            {"Name": "Enco Manufacturing Company", "category": '', "reportTo": 'Dun &amp; Bradstreet', "link": "1"},
            {"Name": "REW Materials", "category": '', "reportTo": 'Equifax Small Business', "link": "2"},
            {"Name": "United Rentals", "category": '', "reportTo": 'Dun &amp; Bradstreet', "link": "3"},
            {"Name": "Copperfield", "category": '', "reportTo": 'Equifax Small Business', "link": "4"},
        ]
        return render(request, 'cooperateCredit/revolving.html', {"list_data": data})


class RevolvingDetailsView(View):
    def get(self, request, state):
        data = {
            "name": "Fleet-One Local Fleet Card",
            "category": '',
            "reportTo": 'Dun &amp; Bradstreet, Experian Business and Equifax Small Business',
            "terms": '',
            "description": ' If your business uses cars, vans or trucks, Fleet-One Local Fuel Cards can make your job \
            easier with security, control, convenience and savings. Use the Fleet-One Local card to pay for fuel and \
            maintenance. With reduced fraud and more control, the savings for your business add up. Approval \
            Requirements: Do not apply for this no personal guarantor account until you have at least 10 reporting \
            trade lines and one trade line with a $10k credit limit reporting. They will check 411 listing, \
            secretary of state for status of your corporation or LLC to make sure it&#39;s in good standing. \
            You&#39;ll need to supply your EIN, copy of a voided business check, copy of a utility bill showing \
            the business address and phone number, and a copy of your business license. (if a business license is \
            required in your state) Leave the personal guarantor section blank.'
        }
        return render(request, 'cooperateCredit/revolving_credit_detail.html', data)


class CCNoGuaranteeVendorList(View):
    def get(self, request):
        data = [
            {"Name": "Enco Manufacturing Company", "category": '', "reportTo": 'Dun &amp; Bradstreet', "link": "1"},
            {"Name": "REW Materials", "category": '', "reportTo": 'Equifax Small Business', "link": "2"},
            {"Name": "United Rentals", "category": '', "reportTo": 'Dun &amp; Bradstreet', "link": "3"},
            {"Name": "Copperfield", "category": '', "reportTo": 'Equifax Small Business', "link": "4"},
        ]
        return render(request, 'cooperateCredit/nopg.html', {"list_data": data})


class NoPgDetailsView(View):
    def get(self, request, state):
        data = {
            "name": "Fleet-One Local Fleet Card",
            "category": '',
            "reportTo": 'Dun &amp; Bradstreet, Experian Business and Equifax Small Business',
            "terms": '',
            "description": ' If your business uses cars, vans or trucks, Fleet-One Local Fuel Cards can make your job easier with security, control, convenience and savings. Use the Fleet-One Local card to pay for fuel and maintenance. With reduced fraud and more control, the savings for your business add up. Approval Requirements: Do not apply for this no personal guarantor account until you have at least 10 reporting trade lines and one trade line with a $10k credit limit reporting. They will check 411 listing, secretary of state for status of your corporation or LLC to make sure it&#39;s in good standing. You&#39;ll need to supply your EIN, copy of a voided business check, copy of a utility bill showing the business address and phone number, and a copy of your business license. (if a business license is required in your state) Leave the personal guarantor section blank.'
        }
        return render(request, 'cooperateCredit/nopg_detail.html', data)


class PersonalCreditCardsView(View):
    def get(self, request):
        return render(request, "financingProducts/personalCreditCard.html")


class BusinessCreditCardsView(View):
    def get(self, request):
        return render(request, "financingProducts/businessCreditCard.html")


class ShortTermLoans(View):
    def get(self, request):
        short_term_loans = ShortTermLoan.objects.all()
        return render(request, "financingProducts/shortTerm.html", {'short_term_loans': short_term_loans})


class BusinessTermLoanView(View):
    def get(self, request):
        business_term_loans = BusinessTermLoan.objects.all()
        return render(request, "financingProducts/businessTermLoan.html", {'business_term_loans': business_term_loans})


class SmallBusinessAdminLoanView(View):
    def get(self, request):
        small_business_loans = SbaLoan.objects.all()
        return render(request, "financingProducts/smallBusinessAdminLoan.html",
                      {'small_business_loans': small_business_loans})


class PersonalLoanView(View):
    def get(self, request):
        return render(request, "financingProducts/personalLoan.html")


class BusinessLineOfCredit(View):
    def get(self, request):
        business_line_credit = LinesOfCredit.objects.all()
        return render(request, "financingProducts/businessLineOfCredit.html",
                      {'business_line_credit': business_line_credit})


class NoCreditCheckFinancing(View):
    def get(self, request):
        return render(request, "financingProducts/noCreditCheckFinancing.html")


class InvoiceFactoring(View):
    def get(self, request):
        return render(request, "financingProducts/invoiceFactoring.html")


class InvoiceFinancing(View):
    def get(self, request):
        return render(request, "financingProducts/invoiceFinancing.html")


class EquipmentFinancing(View):
    def get(self, request):
        return render(request, "financingProducts/equipmentFinancing.html")


class MarketingYourBusiness(View):
    def get(self, request):
        return render(request, 'marketingYourBusiness.html')


class OfferFinancingToCustomer(View):
    def get(self, request):
        return render(request, 'customerFinancing.html')


class ApplyingForLoans(View):
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
