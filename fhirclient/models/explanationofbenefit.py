#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8522 (http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit) on 2016-06-16.
#  2016, SMART Health IT.


from . import domainresource

class ExplanationOfBenefit(domainresource.DomainResource):
    """ Explanation of Benefit resource.
    
    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """
    
    resource_name = "ExplanationOfBenefit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accident = None
        """ None.
        Type `ExplanationOfBenefitAccident` (represented as `dict` in JSON). """
        
        self.addItem = None
        """ Insurer added line items.
        List of `ExplanationOfBenefitAddItem` items (represented as `dict` in JSON). """
        
        self.benefitBalance = None
        """ Balance by Benefit Category.
        List of `ExplanationOfBenefitBenefitBalance` items (represented as `dict` in JSON). """
        
        self.billablePeriod = None
        """ Period for charge submission.
        Type `Period` (represented as `dict` in JSON). """
        
        self.claimIdentifier = None
        """ Claim reference.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.claimReference = None
        """ Claim reference.
        Type `FHIRReference` referencing `Claim` (represented as `dict` in JSON). """
        
        self.claimResponseIdentifier = None
        """ Claim response reference.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.claimResponseReference = None
        """ Claim response reference.
        Type `FHIRReference` referencing `ClaimResponse` (represented as `dict` in JSON). """
        
        self.coverage = None
        """ Insurance or medical plan.
        Type `ExplanationOfBenefitCoverage` (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.diagnosis = None
        """ Diagnosis.
        List of `ExplanationOfBenefitDiagnosis` items (represented as `dict` in JSON). """
        
        self.disposition = None
        """ Disposition Message.
        Type `str`. """
        
        self.employmentImpacted = None
        """ Period unable to work.
        Type `Period` (represented as `dict` in JSON). """
        
        self.facilityIdentifier = None
        """ Servicing Facility.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.facilityReference = None
        """ Servicing Facility.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.form = None
        """ Printed Form Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.hospitalization = None
        """ Period in hospital.
        Type `Period` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.information = None
        """ None.
        List of `ExplanationOfBenefitInformation` items (represented as `dict` in JSON). """
        
        self.item = None
        """ Goods and Services.
        List of `ExplanationOfBenefitItem` items (represented as `dict` in JSON). """
        
        self.missingTeeth = None
        """ Only if type = oral.
        List of `ExplanationOfBenefitMissingTeeth` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Processing notes.
        List of `ExplanationOfBenefitNote` items (represented as `dict` in JSON). """
        
        self.organizationIdentifier = None
        """ Responsible organization for the claim.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.organizationReference = None
        """ Responsible organization for the claim.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalPrescriptionIdentifier = None
        """ Original Prescription.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.originalPrescriptionReference = None
        """ Original Prescription.
        Type `FHIRReference` referencing `MedicationOrder` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original specification followed.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ complete | error | partial.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.patientIdentifier = None
        """ The subject of the Products and Services.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patientReference = None
        """ The subject of the Products and Services.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.payee = None
        """ Payee.
        Type `ExplanationOfBenefitPayee` (represented as `dict` in JSON). """
        
        self.payment = None
        """ None.
        Type `ExplanationOfBenefitPayment` (represented as `dict` in JSON). """
        
        self.precedence = None
        """ Precedence (primary, secondary, etc.).
        Type `int`. """
        
        self.prescriptionIdentifier = None
        """ Prescription.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.prescriptionReference = None
        """ Prescription.
        Type `FHIRReference` referencing `MedicationOrder, VisionPrescription` (represented as `dict` in JSON). """
        
        self.procedure = None
        """ Procedures performed.
        List of `ExplanationOfBenefitProcedure` items (represented as `dict` in JSON). """
        
        self.providerIdentifier = None
        """ Responsible provider for the claim.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.providerReference = None
        """ Responsible provider for the claim.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.referralIdentifier = None
        """ Treatment Referral.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.referralReference = None
        """ Treatment Referral.
        Type `FHIRReference` referencing `ReferralRequest` (represented as `dict` in JSON). """
        
        self.related = None
        """ Related Claims which may be revelant to processing this claimn.
        List of `ExplanationOfBenefitRelated` items (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Current specification followed.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.subType = None
        """ Finer grained claim type information.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.totalBenefit = None
        """ Total benefit payable for the Claim.
        Type `Money` (represented as `dict` in JSON). """
        
        self.totalCost = None
        """ Total Cost of service from the Claim.
        Type `Money` (represented as `dict` in JSON). """
        
        self.type = None
        """ institutional | oral | pharmacy | professional | vision.
        Type `str`. """
        
        self.unallocDeductable = None
        """ Unallocated deductable.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefit, self).elementProperties()
        js.extend([
            ("accident", "accident", ExplanationOfBenefitAccident, False, None, False),
            ("addItem", "addItem", ExplanationOfBenefitAddItem, True, None, False),
            ("benefitBalance", "benefitBalance", ExplanationOfBenefitBenefitBalance, True, None, False),
            ("billablePeriod", "billablePeriod", period.Period, False, None, False),
            ("claimIdentifier", "claimIdentifier", identifier.Identifier, False, "claim", False),
            ("claimReference", "claimReference", fhirreference.FHIRReference, False, "claim", False),
            ("claimResponseIdentifier", "claimResponseIdentifier", identifier.Identifier, False, "claimResponse", False),
            ("claimResponseReference", "claimResponseReference", fhirreference.FHIRReference, False, "claimResponse", False),
            ("coverage", "coverage", ExplanationOfBenefitCoverage, False, None, True),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("diagnosis", "diagnosis", ExplanationOfBenefitDiagnosis, True, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("employmentImpacted", "employmentImpacted", period.Period, False, None, False),
            ("facilityIdentifier", "facilityIdentifier", identifier.Identifier, False, "facility", False),
            ("facilityReference", "facilityReference", fhirreference.FHIRReference, False, "facility", False),
            ("form", "form", coding.Coding, False, None, False),
            ("hospitalization", "hospitalization", period.Period, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("information", "information", ExplanationOfBenefitInformation, True, None, False),
            ("item", "item", ExplanationOfBenefitItem, True, None, False),
            ("missingTeeth", "missingTeeth", ExplanationOfBenefitMissingTeeth, True, None, False),
            ("note", "note", ExplanationOfBenefitNote, True, None, False),
            ("organizationIdentifier", "organizationIdentifier", identifier.Identifier, False, "organization", False),
            ("organizationReference", "organizationReference", fhirreference.FHIRReference, False, "organization", False),
            ("originalPrescriptionIdentifier", "originalPrescriptionIdentifier", identifier.Identifier, False, "originalPrescription", False),
            ("originalPrescriptionReference", "originalPrescriptionReference", fhirreference.FHIRReference, False, "originalPrescription", False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("outcome", "outcome", coding.Coding, False, None, False),
            ("patientIdentifier", "patientIdentifier", identifier.Identifier, False, "patient", True),
            ("patientReference", "patientReference", fhirreference.FHIRReference, False, "patient", True),
            ("payee", "payee", ExplanationOfBenefitPayee, False, None, False),
            ("payment", "payment", ExplanationOfBenefitPayment, False, None, False),
            ("precedence", "precedence", int, False, None, False),
            ("prescriptionIdentifier", "prescriptionIdentifier", identifier.Identifier, False, "prescription", False),
            ("prescriptionReference", "prescriptionReference", fhirreference.FHIRReference, False, "prescription", False),
            ("procedure", "procedure", ExplanationOfBenefitProcedure, True, None, False),
            ("providerIdentifier", "providerIdentifier", identifier.Identifier, False, "provider", False),
            ("providerReference", "providerReference", fhirreference.FHIRReference, False, "provider", False),
            ("referralIdentifier", "referralIdentifier", identifier.Identifier, False, "referral", False),
            ("referralReference", "referralReference", fhirreference.FHIRReference, False, "referral", False),
            ("related", "related", ExplanationOfBenefitRelated, True, None, False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("subType", "subType", coding.Coding, True, None, False),
            ("totalBenefit", "totalBenefit", money.Money, False, None, False),
            ("totalCost", "totalCost", money.Money, False, None, False),
            ("type", "type", str, False, None, True),
            ("unallocDeductable", "unallocDeductable", money.Money, False, None, False),
        ])
        return js


from . import backboneelement

class ExplanationOfBenefitAccident(backboneelement.BackboneElement):
    """ None.
    
    An accident which resulted in the need for healthcare services.
    """
    
    resource_name = "ExplanationOfBenefitAccident"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ When the accident occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.locationAddress = None
        """ Accident Place.
        Type `Address` (represented as `dict` in JSON). """
        
        self.locationReference = None
        """ Accident Place.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.type = None
        """ The nature of the accident.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitAccident, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitAccident, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("type", "type", coding.Coding, False, None, False),
        ])
        return js


class ExplanationOfBenefitAddItem(backboneelement.BackboneElement):
    """ Insurer added line items.
    
    The first tier service adjudications for payor added services.
    """
    
    resource_name = "ExplanationOfBenefitAddItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Added items adjudication.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.detail = None
        """ Added items details.
        List of `ExplanationOfBenefitAddItemDetail` items (represented as `dict` in JSON). """
        
        self.fee = None
        """ Professional fee or Product charge.
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumberLinkId = None
        """ List of note numbers which apply.
        List of `int` items. """
        
        self.sequenceLinkId = None
        """ Service instances.
        List of `int` items. """
        
        self.service = None
        """ Group, Service or Product.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitAddItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("detail", "detail", ExplanationOfBenefitAddItemDetail, True, None, False),
            ("fee", "fee", money.Money, False, None, False),
            ("noteNumberLinkId", "noteNumberLinkId", int, True, None, False),
            ("sequenceLinkId", "sequenceLinkId", int, True, None, False),
            ("service", "service", coding.Coding, False, None, True),
        ])
        return js


class ExplanationOfBenefitAddItemDetail(backboneelement.BackboneElement):
    """ Added items details.
    
    The second tier service adjudications for payor added services.
    """
    
    resource_name = "ExplanationOfBenefitAddItemDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Added items detail adjudication.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.fee = None
        """ Professional fee or Product charge.
        Type `Money` (represented as `dict` in JSON). """
        
        self.service = None
        """ Service or Product.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitAddItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("fee", "fee", money.Money, False, None, False),
            ("service", "service", coding.Coding, False, None, True),
        ])
        return js


class ExplanationOfBenefitBenefitBalance(backboneelement.BackboneElement):
    """ Balance by Benefit Category.
    """
    
    resource_name = "ExplanationOfBenefitBenefitBalance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Benefit Category.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.financial = None
        """ Benefit Summary.
        List of `ExplanationOfBenefitBenefitBalanceFinancial` items (represented as `dict` in JSON). """
        
        self.network = None
        """ In or out of network.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.subCategory = None
        """ Benefit SubCategory.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.term = None
        """ Annual or lifetime.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.unit = None
        """ Individual or family.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitBenefitBalance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitBenefitBalance, self).elementProperties()
        js.extend([
            ("category", "category", coding.Coding, False, None, True),
            ("financial", "financial", ExplanationOfBenefitBenefitBalanceFinancial, True, None, False),
            ("network", "network", coding.Coding, False, None, False),
            ("subCategory", "subCategory", coding.Coding, False, None, False),
            ("term", "term", coding.Coding, False, None, False),
            ("unit", "unit", coding.Coding, False, None, False),
        ])
        return js


class ExplanationOfBenefitBenefitBalanceFinancial(backboneelement.BackboneElement):
    """ Benefit Summary.
    
    Benefits Used to date.
    """
    
    resource_name = "ExplanationOfBenefitBenefitBalanceFinancial"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.benefitMoney = None
        """ Benefits allowed.
        Type `Money` (represented as `dict` in JSON). """
        
        self.benefitUnsignedInt = None
        """ Benefits allowed.
        Type `int`. """
        
        self.benefitUsedMoney = None
        """ Benefits used.
        Type `Money` (represented as `dict` in JSON). """
        
        self.benefitUsedUnsignedInt = None
        """ Benefits used.
        Type `int`. """
        
        self.type = None
        """ Deductable, visits, benefit amount.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitBenefitBalanceFinancial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitBenefitBalanceFinancial, self).elementProperties()
        js.extend([
            ("benefitMoney", "benefitMoney", money.Money, False, "benefit", False),
            ("benefitUnsignedInt", "benefitUnsignedInt", int, False, "benefit", False),
            ("benefitUsedMoney", "benefitUsedMoney", money.Money, False, "benefitUsed", False),
            ("benefitUsedUnsignedInt", "benefitUsedUnsignedInt", int, False, "benefitUsed", False),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js


class ExplanationOfBenefitCoverage(backboneelement.BackboneElement):
    """ Insurance or medical plan.
    
    Financial instrument by which payment information for health care.
    """
    
    resource_name = "ExplanationOfBenefitCoverage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coverageIdentifier = None
        """ Insurance information.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.coverageReference = None
        """ Insurance information.
        Type `FHIRReference` referencing `Coverage` (represented as `dict` in JSON). """
        
        self.preAuthRef = None
        """ Pre-Authorization/Determination Reference.
        List of `str` items. """
        
        super(ExplanationOfBenefitCoverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitCoverage, self).elementProperties()
        js.extend([
            ("coverageIdentifier", "coverageIdentifier", identifier.Identifier, False, "coverage", False),
            ("coverageReference", "coverageReference", fhirreference.FHIRReference, False, "coverage", False),
            ("preAuthRef", "preAuthRef", str, True, None, False),
        ])
        return js


class ExplanationOfBenefitDiagnosis(backboneelement.BackboneElement):
    """ Diagnosis.
    
    Ordered list of patient diagnosis for which care is sought.
    """
    
    resource_name = "ExplanationOfBenefitDiagnosis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.diagnosis = None
        """ Patient's list of diagnosis.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.drg = None
        """ Diagnosis Related Group.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Number to covey order of diagnosis.
        Type `int`. """
        
        self.type = None
        """ Type of Diagnosis.
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosis", "diagnosis", coding.Coding, False, None, True),
            ("drg", "drg", coding.Coding, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("type", "type", coding.Coding, True, None, False),
        ])
        return js


class ExplanationOfBenefitInformation(backboneelement.BackboneElement):
    """ None.
    
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues. Often there are
    mutiple jurisdiction specific valuesets which are required.
    """
    
    resource_name = "ExplanationOfBenefitInformation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Type of information.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.timingDate = None
        """ When it occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod = None
        """ When it occurred.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Additional Data.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ Additional Data.
        Type `str`. """
        
        super(ExplanationOfBenefitInformation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitInformation, self).elementProperties()
        js.extend([
            ("code", "code", coding.Coding, False, None, False),
            ("timingDate", "timingDate", fhirdate.FHIRDate, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
        ])
        return js


class ExplanationOfBenefitItem(backboneelement.BackboneElement):
    """ Goods and Services.
    
    First tier of goods and services.
    """
    
    resource_name = "ExplanationOfBenefitItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Adjudication details.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Service Location.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.careTeam = None
        """ None.
        List of `ExplanationOfBenefitItemCareTeam` items (represented as `dict` in JSON). """
        
        self.detail = None
        """ Additional items.
        List of `ExplanationOfBenefitItemDetail` items (represented as `dict` in JSON). """
        
        self.diagnosisLinkId = None
        """ Applicable diagnoses.
        List of `int` items. """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.modifier = None
        """ Service/Product billing modifiers.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.net = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber = None
        """ List of note numbers which apply.
        List of `int` items. """
        
        self.place = None
        """ Place of service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.points = None
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.programCode = None
        """ Program specific reason for item inclusion.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.prosthesis = None
        """ Prosthetic details.
        Type `ExplanationOfBenefitItemProsthesis` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        self.service = None
        """ Item Code.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.serviceModifier = None
        """ Service/Product modifiers.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.servicedDate = None
        """ Date or dates of Service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        """ Date or dates of Service.
        Type `Period` (represented as `dict` in JSON). """
        
        self.subSite = None
        """ Service Sub-location.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Group or type of product or service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique Device Identifier.
        List of `FHIRReference` items referencing `Device` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("bodySite", "bodySite", coding.Coding, False, None, False),
            ("careTeam", "careTeam", ExplanationOfBenefitItemCareTeam, True, None, False),
            ("detail", "detail", ExplanationOfBenefitItemDetail, True, None, False),
            ("diagnosisLinkId", "diagnosisLinkId", int, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", coding.Coding, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("place", "place", coding.Coding, False, None, False),
            ("points", "points", float, False, None, False),
            ("programCode", "programCode", coding.Coding, True, None, False),
            ("prosthesis", "prosthesis", ExplanationOfBenefitItemProsthesis, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("service", "service", coding.Coding, False, None, True),
            ("serviceModifier", "serviceModifier", coding.Coding, True, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("subSite", "subSite", coding.Coding, True, None, False),
            ("type", "type", coding.Coding, False, None, True),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemAdjudication(backboneelement.BackboneElement):
    """ Adjudication details.
    
    The adjudications results.
    """
    
    resource_name = "ExplanationOfBenefitItemAdjudication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Monetary amount.
        Type `Money` (represented as `dict` in JSON). """
        
        self.category = None
        """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Adjudication reason.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ Non-monitory value.
        Type `float`. """
        
        super(ExplanationOfBenefitItemAdjudication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitItemAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("category", "category", coding.Coding, False, None, True),
            ("reason", "reason", coding.Coding, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemCareTeam(backboneelement.BackboneElement):
    """ None.
    
    The members of the team who provided the overall service as well as their
    role and whether responsible and qualifications.
    """
    
    resource_name = "ExplanationOfBenefitItemCareTeam"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.providerIdentifier = None
        """ None.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.providerReference = None
        """ None.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.qualification = None
        """ Type, classification or Specialization.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.responsible = None
        """ Billing practitioner.
        Type `bool`. """
        
        self.role = None
        """ Role on the team.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitItemCareTeam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitItemCareTeam, self).elementProperties()
        js.extend([
            ("providerIdentifier", "providerIdentifier", identifier.Identifier, False, "provider", True),
            ("providerReference", "providerReference", fhirreference.FHIRReference, False, "provider", True),
            ("qualification", "qualification", coding.Coding, False, None, False),
            ("responsible", "responsible", bool, False, None, False),
            ("role", "role", coding.Coding, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Second tier of goods and services.
    """
    
    resource_name = "ExplanationOfBenefitItemDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Detail adjudication.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.net = None
        """ Total additional item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.points = None
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.programCode = None
        """ Program specific reason for item inclusion.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        self.service = None
        """ Additional item codes.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.subDetail = None
        """ Additional items.
        List of `ExplanationOfBenefitItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Group or type of product or service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique Device Identifier.
        List of `FHIRReference` items referencing `Device` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("net", "net", money.Money, False, None, False),
            ("points", "points", float, False, None, False),
            ("programCode", "programCode", coding.Coding, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("service", "service", coding.Coding, False, None, True),
            ("subDetail", "subDetail", ExplanationOfBenefitItemDetailSubDetail, True, None, False),
            ("type", "type", coding.Coding, False, None, True),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemDetailSubDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Third tier of goods and services.
    """
    
    resource_name = "ExplanationOfBenefitItemDetailSubDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ SubDetail adjudication.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.net = None
        """ Net additional item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.points = None
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.programCode = None
        """ Program specific reason for item inclusion.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        self.service = None
        """ Additional item codes.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of product or service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique Device Identifier.
        List of `FHIRReference` items referencing `Device` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("net", "net", money.Money, False, None, False),
            ("points", "points", float, False, None, False),
            ("programCode", "programCode", coding.Coding, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("service", "service", coding.Coding, False, None, True),
            ("type", "type", coding.Coding, False, None, True),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemProsthesis(backboneelement.BackboneElement):
    """ Prosthetic details.
    
    The materials and placement date of prior fixed prosthesis.
    """
    
    resource_name = "ExplanationOfBenefitItemProsthesis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.initial = None
        """ Is this the initial service.
        Type `bool`. """
        
        self.priorDate = None
        """ Initial service Date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.priorMaterial = None
        """ Prosthetic Material.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitItemProsthesis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitItemProsthesis, self).elementProperties()
        js.extend([
            ("initial", "initial", bool, False, None, False),
            ("priorDate", "priorDate", fhirdate.FHIRDate, False, None, False),
            ("priorMaterial", "priorMaterial", coding.Coding, False, None, False),
        ])
        return js


class ExplanationOfBenefitMissingTeeth(backboneelement.BackboneElement):
    """ Only if type = oral.
    
    A list of teeth which would be expected but are not found due to having
    been previously  extracted or for other reasons.
    """
    
    resource_name = "ExplanationOfBenefitMissingTeeth"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.extractionDate = None
        """ Date of Extraction.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.reason = None
        """ Reason for missing.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.tooth = None
        """ Tooth Code.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitMissingTeeth, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitMissingTeeth, self).elementProperties()
        js.extend([
            ("extractionDate", "extractionDate", fhirdate.FHIRDate, False, None, False),
            ("reason", "reason", coding.Coding, False, None, False),
            ("tooth", "tooth", coding.Coding, False, None, True),
        ])
        return js


class ExplanationOfBenefitNote(backboneelement.BackboneElement):
    """ Processing notes.
    
    Note text.
    """
    
    resource_name = "ExplanationOfBenefitNote"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.number = None
        """ Note Number for this note.
        Type `int`. """
        
        self.text = None
        """ Note explanitory text.
        Type `str`. """
        
        self.type = None
        """ display | print | printoper.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitNote, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitNote, self).elementProperties()
        js.extend([
            ("number", "number", int, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
        ])
        return js


class ExplanationOfBenefitPayee(backboneelement.BackboneElement):
    """ Payee.
    
    The party to be reimbursed for the services.
    """
    
    resource_name = "ExplanationOfBenefitPayee"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.partyIdentifier = None
        """ Party to receive the payable.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.partyReference = None
        """ Party to receive the payable.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.resourceType = None
        """ organization | patient | practitioner | relatedperson.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of party: Subscriber, Provider, other.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitPayee, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitPayee, self).elementProperties()
        js.extend([
            ("partyIdentifier", "partyIdentifier", identifier.Identifier, False, "party", False),
            ("partyReference", "partyReference", fhirreference.FHIRReference, False, "party", False),
            ("resourceType", "resourceType", coding.Coding, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
        ])
        return js


class ExplanationOfBenefitPayment(backboneelement.BackboneElement):
    """ None.
    
    Payment details for the claim if the claim has been paid.
    """
    
    resource_name = "ExplanationOfBenefitPayment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjustment = None
        """ Payment adjustment for non-Claim issues.
        Type `Money` (represented as `dict` in JSON). """
        
        self.adjustmentReason = None
        """ Reason for Payment adjustment.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.amount = None
        """ Payment amount.
        Type `Money` (represented as `dict` in JSON). """
        
        self.date = None
        """ Expected date of Payment.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Payment identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type = None
        """ Partial or Complete.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitPayment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitPayment, self).elementProperties()
        js.extend([
            ("adjustment", "adjustment", money.Money, False, None, False),
            ("adjustmentReason", "adjustmentReason", coding.Coding, False, None, False),
            ("amount", "amount", money.Money, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
        ])
        return js


class ExplanationOfBenefitProcedure(backboneelement.BackboneElement):
    """ Procedures performed.
    
    Ordered list of patient procedures performed to support the adjudication.
    """
    
    resource_name = "ExplanationOfBenefitProcedure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ When the procedure was performed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.procedureCoding = None
        """ Patient's list of procedures performed.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.procedureReference = None
        """ Patient's list of procedures performed.
        Type `FHIRReference` referencing `Procedure` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Procedure sequence for reference.
        Type `int`. """
        
        super(ExplanationOfBenefitProcedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitProcedure, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("procedureCoding", "procedureCoding", coding.Coding, False, "procedure", True),
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, False, "procedure", True),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


class ExplanationOfBenefitRelated(backboneelement.BackboneElement):
    """ Related Claims which may be revelant to processing this claimn.
    
    Other claims which are related to this claim such as prior claim versions
    or for related services.
    """
    
    resource_name = "ExplanationOfBenefitRelated"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.claimIdentifier = None
        """ Reference to the related claim.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.claimReference = None
        """ Reference to the related claim.
        Type `FHIRReference` referencing `Claim` (represented as `dict` in JSON). """
        
        self.reference = None
        """ Related file or case reference.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ How the reference claim is related.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitRelated, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitRelated, self).elementProperties()
        js.extend([
            ("claimIdentifier", "claimIdentifier", identifier.Identifier, False, "claim", False),
            ("claimReference", "claimReference", fhirreference.FHIRReference, False, "claim", False),
            ("reference", "reference", identifier.Identifier, False, None, False),
            ("relationship", "relationship", coding.Coding, False, None, False),
        ])
        return js


from . import address
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity
