#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8522 on 2016-06-16.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import claim
from .fhirdate import FHIRDate


class ClaimTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Claim", js["resourceType"])
        return claim.Claim(js)
    
    def testClaim1(self):
        inst = self.instantiate_from("claim-example-institutional.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim1(inst)
        
        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim1(inst2)
    
    def implClaim1(self, inst):
        self.assertTrue(inst.coverage[0].focal)
        self.assertEqual(inst.coverage[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.diagnosis[0].diagnosis.code, "654456")
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(inst.entererIdentifier.system, "http://jurisdiction.org/facilities/HOSP1234/users")
        self.assertEqual(inst.entererIdentifier.value, "UC1234")
        self.assertEqual(inst.facilityIdentifier.system, "http://jurisdiction.org/facilities")
        self.assertEqual(inst.facilityIdentifier.value, "HOSP1234")
        self.assertEqual(inst.id, "960150")
        self.assertEqual(inst.identifier[0].system, "http://happyhospital.com/claim")
        self.assertEqual(inst.identifier[0].value, "9612345")
        self.assertEqual(inst.item[0].net.code, "USD")
        self.assertEqual(inst.item[0].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].net.value, 125.0)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(inst.item[0].service.code, "exam")
        self.assertEqual(inst.item[0].service.system, "http://hl7.org/fhir/ex-serviceproduct")
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(inst.item[0].type.code, "service")
        self.assertEqual(inst.item[0].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].unitPrice.value, 125.0)
        self.assertEqual(inst.payee.type.code, "provider")
        self.assertEqual(inst.priority.code, "normal")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Claim</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.total.code, "USD")
        self.assertEqual(inst.total.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.total.value, 125.0)
        self.assertEqual(inst.type, "institutional")
        self.assertEqual(inst.use, "complete")
    
    def testClaim2(self):
        inst = self.instantiate_from("claim-example-oral-average.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim2(inst)
        
        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim2(inst2)
    
    def implClaim2(self, inst):
        self.assertTrue(inst.coverage[0].focal)
        self.assertEqual(inst.coverage[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.diagnosis[0].diagnosis.code, "123456")
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(inst.id, "100151")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/claim")
        self.assertEqual(inst.identifier[0].value, "12346")
        self.assertEqual(inst.item[0].net.code, "USD")
        self.assertEqual(inst.item[0].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].net.value, 135.57)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(inst.item[0].service.code, "1200")
        self.assertEqual(inst.item[0].service.system, "http://hl7.org/fhir/oralservicecodes")
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(inst.item[0].type.code, "service")
        self.assertEqual(inst.item[0].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].unitPrice.value, 135.57)
        self.assertEqual(inst.item[1].bodySite.code, "21")
        self.assertEqual(inst.item[1].bodySite.system, "http://fdi.org/fhir/oraltoothcodes")
        self.assertEqual(inst.item[1].net.code, "USD")
        self.assertEqual(inst.item[1].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[1].net.value, 105.0)
        self.assertEqual(inst.item[1].sequence, 2)
        self.assertEqual(inst.item[1].service.code, "21211")
        self.assertEqual(inst.item[1].service.system, "http://hl7.org/fhir/oralservicecodes")
        self.assertEqual(inst.item[1].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[1].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(inst.item[1].subSite[0].code, "L")
        self.assertEqual(inst.item[1].subSite[0].system, "http://fdi.org/fhir/oralsurfacecodes")
        self.assertEqual(inst.item[1].type.code, "service")
        self.assertEqual(inst.item[1].unitPrice.code, "USD")
        self.assertEqual(inst.item[1].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[1].unitPrice.value, 105.0)
        self.assertEqual(inst.item[2].bodySite.code, "36")
        self.assertEqual(inst.item[2].bodySite.system, "http://fdi.org/fhir/oraltoothcodes")
        self.assertEqual(inst.item[2].detail[0].net.code, "USD")
        self.assertEqual(inst.item[2].detail[0].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[2].detail[0].net.value, 750.0)
        self.assertEqual(inst.item[2].detail[0].sequence, 1)
        self.assertEqual(inst.item[2].detail[0].service.code, "27211")
        self.assertEqual(inst.item[2].detail[0].service.system, "http://hl7.org/fhir/oralservicecodes")
        self.assertEqual(inst.item[2].detail[0].type.code, "service")
        self.assertEqual(inst.item[2].detail[0].unitPrice.code, "USD")
        self.assertEqual(inst.item[2].detail[0].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[2].detail[0].unitPrice.value, 750.0)
        self.assertEqual(inst.item[2].detail[1].net.code, "USD")
        self.assertEqual(inst.item[2].detail[1].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[2].detail[1].net.value, 350.0)
        self.assertEqual(inst.item[2].detail[1].sequence, 2)
        self.assertEqual(inst.item[2].detail[1].service.code, "lab")
        self.assertEqual(inst.item[2].detail[1].service.system, "http://hl7.org/fhir/oralservicecodes")
        self.assertEqual(inst.item[2].detail[1].type.code, "service")
        self.assertEqual(inst.item[2].detail[1].unitPrice.code, "USD")
        self.assertEqual(inst.item[2].detail[1].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[2].detail[1].unitPrice.value, 350.0)
        self.assertEqual(inst.item[2].net.code, "USD")
        self.assertEqual(inst.item[2].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[2].net.value, 1100.0)
        self.assertEqual(inst.item[2].sequence, 3)
        self.assertEqual(inst.item[2].service.code, "27211")
        self.assertEqual(inst.item[2].service.system, "http://hl7.org/fhir/oralservicecodes")
        self.assertEqual(inst.item[2].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[2].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(inst.item[2].type.code, "group")
        self.assertEqual(inst.item[2].unitPrice.code, "USD")
        self.assertEqual(inst.item[2].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[2].unitPrice.value, 1100.0)
        self.assertEqual(inst.payee.type.code, "provider")
        self.assertEqual(inst.priority.code, "normal")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Oral Health Claim</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "oral")
        self.assertEqual(inst.use, "complete")
    
    def testClaim3(self):
        inst = self.instantiate_from("claim-example-oral-contained-identifier.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim3(inst)
        
        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim3(inst2)
    
    def implClaim3(self, inst):
        self.assertEqual(inst.contained[0].id, "patient-1")
        self.assertEqual(inst.coverage[0].coverageIdentifier.system, "http://www.jurisdiction.com/nationalplan")
        self.assertEqual(inst.coverage[0].coverageIdentifier.value, "123AB345")
        self.assertTrue(inst.coverage[0].focal)
        self.assertEqual(inst.coverage[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.diagnosis[0].diagnosis.code, "123456")
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(inst.id, "100155")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/claim")
        self.assertEqual(inst.identifier[0].value, "12347")
        self.assertEqual(inst.item[0].careTeam[0].providerIdentifier.system, "http://www.jurisdiction.com/providerId")
        self.assertEqual(inst.item[0].careTeam[0].providerIdentifier.value, "MD98765")
        self.assertEqual(inst.item[0].net.code, "USD")
        self.assertEqual(inst.item[0].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].net.value, 135.57)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(inst.item[0].service.code, "1200")
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(inst.item[0].type.code, "service")
        self.assertEqual(inst.item[0].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].unitPrice.value, 135.57)
        self.assertEqual(inst.organizationIdentifier.system, "http://www.jurisdiction.com/careorganizations")
        self.assertEqual(inst.organizationIdentifier.value, "HOSP12345")
        self.assertEqual(inst.payee.type.code, "provider")
        self.assertEqual(inst.priority.code, "normal")
        self.assertEqual(inst.targetIdentifier.system, "http://www.jurisdiction.com/insurers")
        self.assertEqual(inst.targetIdentifier.value, "123456")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">This example assumes a national health care scheme where patients, providers and organizations have known business identifiers.</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "oral")
        self.assertEqual(inst.use, "complete")
    
    def testClaim4(self):
        inst = self.instantiate_from("claim-example-oral-contained.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim4(inst)
        
        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim4(inst2)
    
    def implClaim4(self, inst):
        self.assertEqual(inst.contained[0].id, "organization-1")
        self.assertEqual(inst.contained[1].id, "organization-2")
        self.assertEqual(inst.contained[2].id, "practitioner-1")
        self.assertEqual(inst.contained[3].id, "patient-1")
        self.assertEqual(inst.contained[4].id, "coverage-1")
        self.assertTrue(inst.coverage[0].focal)
        self.assertEqual(inst.coverage[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.diagnosis[0].diagnosis.code, "123456")
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(inst.id, "100152")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/claim")
        self.assertEqual(inst.identifier[0].value, "12347")
        self.assertEqual(inst.item[0].net.code, "USD")
        self.assertEqual(inst.item[0].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].net.value, 135.57)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(inst.item[0].service.code, "1200")
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(inst.item[0].type.code, "service")
        self.assertEqual(inst.item[0].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].unitPrice.value, 135.57)
        self.assertEqual(inst.payee.type.code, "provider")
        self.assertEqual(inst.priority.code, "normal")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Oral Health Claim</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "oral")
        self.assertEqual(inst.use, "complete")
    
    def testClaim5(self):
        inst = self.instantiate_from("claim-example-oral-identifier.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim5(inst)
        
        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim5(inst2)
    
    def implClaim5(self, inst):
        self.assertEqual(inst.coverage[0].coverageIdentifier.system, "http://www.jurisdiction.com/nationalplan")
        self.assertEqual(inst.coverage[0].coverageIdentifier.value, "123AB345")
        self.assertTrue(inst.coverage[0].focal)
        self.assertEqual(inst.coverage[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.diagnosis[0].diagnosis.code, "123456")
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(inst.id, "100154")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/claim")
        self.assertEqual(inst.identifier[0].value, "12347")
        self.assertEqual(inst.item[0].careTeam[0].providerIdentifier.system, "http://www.jurisdiction.com/providerId")
        self.assertEqual(inst.item[0].careTeam[0].providerIdentifier.value, "MD98765")
        self.assertEqual(inst.item[0].net.code, "USD")
        self.assertEqual(inst.item[0].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].net.value, 135.57)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(inst.item[0].service.code, "1200")
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(inst.item[0].type.code, "service")
        self.assertEqual(inst.item[0].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].unitPrice.value, 135.57)
        self.assertEqual(inst.organizationIdentifier.system, "http://www.jurisdiction.com/careorganizations")
        self.assertEqual(inst.organizationIdentifier.value, "HOSP12345")
        self.assertEqual(inst.patientIdentifier.system, "http://www.jurisdiction.com/nationalId")
        self.assertEqual(inst.patientIdentifier.value, "123AB345")
        self.assertEqual(inst.payee.type.code, "provider")
        self.assertEqual(inst.priority.code, "normal")
        self.assertEqual(inst.targetIdentifier.system, "http://www.jurisdiction.com/insurers")
        self.assertEqual(inst.targetIdentifier.value, "123456")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">This example assumes a national health care scheme where patients, providers and organizations have known business identifiers.</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "oral")
        self.assertEqual(inst.use, "complete")
    
    def testClaim6(self):
        inst = self.instantiate_from("claim-example-oral-orthoplan.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim6(inst)
        
        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim6(inst2)
    
    def implClaim6(self, inst):
        self.assertTrue(inst.coverage[0].focal)
        self.assertEqual(inst.coverage[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2015-03-16").date)
        self.assertEqual(inst.created.as_json(), "2015-03-16")
        self.assertEqual(inst.diagnosis[0].diagnosis.code, "123457")
        self.assertEqual(inst.diagnosis[0].diagnosis.system, "http://hl7.org/fhir/sid/icd-10")
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(inst.fundsReserve.code, "provider")
        self.assertEqual(inst.id, "100153")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/claim")
        self.assertEqual(inst.identifier[0].value, "12355")
        self.assertEqual(inst.item[0].detail[0].net.code, "USD")
        self.assertEqual(inst.item[0].detail[0].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].detail[0].net.value, 1000.0)
        self.assertEqual(inst.item[0].detail[0].sequence, 1)
        self.assertEqual(inst.item[0].detail[0].service.code, "ORTHOEXAM")
        self.assertEqual(inst.item[0].detail[0].service.system, "http://hl7.org/fhir/oralservicecodes")
        self.assertEqual(inst.item[0].detail[0].type.code, "CSINV")
        self.assertEqual(inst.item[0].detail[0].type.system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.item[0].detail[0].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].detail[0].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].detail[0].unitPrice.value, 1000.0)
        self.assertEqual(inst.item[0].detail[1].net.code, "USD")
        self.assertEqual(inst.item[0].detail[1].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].detail[1].net.value, 1500.0)
        self.assertEqual(inst.item[0].detail[1].sequence, 2)
        self.assertEqual(inst.item[0].detail[1].service.code, "ORTHODIAG")
        self.assertEqual(inst.item[0].detail[1].service.system, "http://hl7.org/fhir/oralservicecodes")
        self.assertEqual(inst.item[0].detail[1].type.code, "CSINV")
        self.assertEqual(inst.item[0].detail[1].type.system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.item[0].detail[1].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].detail[1].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].detail[1].unitPrice.value, 1500.0)
        self.assertEqual(inst.item[0].detail[2].net.code, "USD")
        self.assertEqual(inst.item[0].detail[2].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].detail[2].net.value, 500.0)
        self.assertEqual(inst.item[0].detail[2].sequence, 3)
        self.assertEqual(inst.item[0].detail[2].service.code, "ORTHOINITIAL")
        self.assertEqual(inst.item[0].detail[2].service.system, "http://hl7.org/fhir/oralservicecodes")
        self.assertEqual(inst.item[0].detail[2].type.code, "CSINV")
        self.assertEqual(inst.item[0].detail[2].type.system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.item[0].detail[2].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].detail[2].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].detail[2].unitPrice.value, 500.0)
        self.assertEqual(inst.item[0].detail[3].quantity.value, 24)
        self.assertEqual(inst.item[0].detail[3].sequence, 4)
        self.assertEqual(inst.item[0].detail[3].service.code, "ORTHOMONTHS")
        self.assertEqual(inst.item[0].detail[3].service.system, "http://hl7.org/fhir/oralservicecodes")
        self.assertEqual(inst.item[0].detail[3].type.code, "CSINV")
        self.assertEqual(inst.item[0].detail[3].type.system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.item[0].detail[4].net.code, "USD")
        self.assertEqual(inst.item[0].detail[4].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].detail[4].net.value, 250.0)
        self.assertEqual(inst.item[0].detail[4].quantity.value, 24)
        self.assertEqual(inst.item[0].detail[4].sequence, 5)
        self.assertEqual(inst.item[0].detail[4].service.code, "ORTHOPERIODIC")
        self.assertEqual(inst.item[0].detail[4].service.system, "http://hl7.org/fhir/oralservicecodes")
        self.assertEqual(inst.item[0].detail[4].type.code, "CSINV")
        self.assertEqual(inst.item[0].detail[4].type.system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.item[0].detail[4].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].detail[4].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].detail[4].unitPrice.value, 250.0)
        self.assertEqual(inst.item[0].diagnosisLinkId[0], 1)
        self.assertEqual(inst.item[0].net.code, "USD")
        self.assertEqual(inst.item[0].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].net.value, 9000.0)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(inst.item[0].service.code, "ORTHPLAN")
        self.assertEqual(inst.item[0].service.system, "http://hl7.org/fhir/oralservicecodes")
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2015-05-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2015-05-16")
        self.assertEqual(inst.item[0].type.code, "FRAMEING")
        self.assertEqual(inst.item[0].type.system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.item[0].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].unitPrice.value, 9000.0)
        self.assertEqual(inst.item[1].bodySite.code, "21")
        self.assertEqual(inst.item[1].bodySite.system, "http://fdi.org/fhir/oraltoothcodes")
        self.assertEqual(inst.item[1].net.code, "USD")
        self.assertEqual(inst.item[1].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[1].net.value, 105.0)
        self.assertEqual(inst.item[1].sequence, 2)
        self.assertEqual(inst.item[1].service.code, "21211")
        self.assertEqual(inst.item[1].service.system, "http://hl7.org/fhir/oralservicecodes")
        self.assertEqual(inst.item[1].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[1].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(inst.item[1].subSite[0].code, "L")
        self.assertEqual(inst.item[1].subSite[0].system, "http://fdi.org/fhir/oralsurfacecodes")
        self.assertEqual(inst.item[1].type.code, "service")
        self.assertEqual(inst.item[1].unitPrice.code, "USD")
        self.assertEqual(inst.item[1].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[1].unitPrice.value, 105.0)
        self.assertEqual(inst.item[2].bodySite.code, "36")
        self.assertEqual(inst.item[2].bodySite.system, "http://fdi.org/fhir/oraltoothcodes")
        self.assertEqual(inst.item[2].detail[0].net.code, "USD")
        self.assertEqual(inst.item[2].detail[0].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[2].detail[0].net.value, 750.0)
        self.assertEqual(inst.item[2].detail[0].sequence, 1)
        self.assertEqual(inst.item[2].detail[0].service.code, "27211")
        self.assertEqual(inst.item[2].detail[0].service.system, "http://hl7.org/fhir/oralservicecodes")
        self.assertEqual(inst.item[2].detail[0].type.code, "service")
        self.assertEqual(inst.item[2].detail[0].unitPrice.code, "USD")
        self.assertEqual(inst.item[2].detail[0].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[2].detail[0].unitPrice.value, 750.0)
        self.assertEqual(inst.item[2].detail[1].net.code, "USD")
        self.assertEqual(inst.item[2].detail[1].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[2].detail[1].net.value, 350.0)
        self.assertEqual(inst.item[2].detail[1].sequence, 2)
        self.assertEqual(inst.item[2].detail[1].service.code, "lab")
        self.assertEqual(inst.item[2].detail[1].service.system, "http://hl7.org/fhir/oralservicecodes")
        self.assertEqual(inst.item[2].detail[1].type.code, "service")
        self.assertEqual(inst.item[2].detail[1].unitPrice.code, "USD")
        self.assertEqual(inst.item[2].detail[1].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[2].detail[1].unitPrice.value, 350.0)
        self.assertEqual(inst.item[2].net.code, "USD")
        self.assertEqual(inst.item[2].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[2].net.value, 1100.0)
        self.assertEqual(inst.item[2].sequence, 3)
        self.assertEqual(inst.item[2].service.code, "27211")
        self.assertEqual(inst.item[2].service.system, "http://hl7.org/fhir/oralservicecodes")
        self.assertEqual(inst.item[2].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[2].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(inst.item[2].type.code, "group")
        self.assertEqual(inst.item[2].unitPrice.code, "USD")
        self.assertEqual(inst.item[2].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[2].unitPrice.value, 1100.0)
        self.assertEqual(inst.payee.type.code, "provider")
        self.assertEqual(inst.priority.code, "normal")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Oral Health Claim</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "oral")
        self.assertEqual(inst.use, "proposed")
    
    def testClaim7(self):
        inst = self.instantiate_from("claim-example-pharmacy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim7(inst)
        
        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim7(inst2)
    
    def implClaim7(self, inst):
        self.assertTrue(inst.coverage[0].focal)
        self.assertEqual(inst.coverage[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.diagnosis[0].diagnosis.code, "654456")
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(inst.id, "760150")
        self.assertEqual(inst.identifier[0].system, "http://happypharma.com/claim")
        self.assertEqual(inst.identifier[0].value, "7612345")
        self.assertEqual(inst.item[0].net.code, "USD")
        self.assertEqual(inst.item[0].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].net.value, 60.0)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(inst.item[0].service.code, "smokecess")
        self.assertEqual(inst.item[0].service.system, "http://hl7.org/fhir/ex-pharmaservice")
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(inst.item[0].type.code, "service")
        self.assertEqual(inst.item[0].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].unitPrice.value, 60.0)
        self.assertEqual(inst.payee.type.code, "provider")
        self.assertEqual(inst.priority.code, "stat")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Pharmacy Claim</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "pharmacy")
        self.assertEqual(inst.use, "complete")
    
    def testClaim8(self):
        inst = self.instantiate_from("claim-example-professional.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim8(inst)
        
        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim8(inst2)
    
    def implClaim8(self, inst):
        self.assertTrue(inst.coverage[0].focal)
        self.assertEqual(inst.coverage[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.diagnosis[0].diagnosis.code, "654456")
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(inst.id, "860150")
        self.assertEqual(inst.identifier[0].system, "http://happypdocs.com/claim")
        self.assertEqual(inst.identifier[0].value, "8612345")
        self.assertEqual(inst.item[0].net.code, "USD")
        self.assertEqual(inst.item[0].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].net.value, 75.0)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(inst.item[0].service.code, "exam")
        self.assertEqual(inst.item[0].service.system, "http://hl7.org/fhir/ex-serviceproduct")
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(inst.item[0].type.code, "service")
        self.assertEqual(inst.item[0].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].unitPrice.value, 75.0)
        self.assertEqual(inst.payee.type.code, "provider")
        self.assertEqual(inst.priority.code, "normal")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Claim</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "professional")
        self.assertEqual(inst.use, "complete")
    
    def testClaim9(self):
        inst = self.instantiate_from("claim-example-vision-glasses.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim9(inst)
        
        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim9(inst2)
    
    def implClaim9(self, inst):
        self.assertTrue(inst.coverage[0].focal)
        self.assertEqual(inst.coverage[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.diagnosis[0].diagnosis.code, "654321")
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(inst.id, "660151")
        self.assertEqual(inst.identifier[0].system, "http://happysight.com/claim")
        self.assertEqual(inst.identifier[0].value, "6612346")
        self.assertEqual(inst.item[0].detail[0].net.code, "USD")
        self.assertEqual(inst.item[0].detail[0].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].detail[0].net.value, 100.0)
        self.assertEqual(inst.item[0].detail[0].sequence, 1)
        self.assertEqual(inst.item[0].detail[0].service.code, "frame")
        self.assertEqual(inst.item[0].detail[0].service.system, "http://hl7.org/fhir/ex-visionservice")
        self.assertEqual(inst.item[0].detail[0].type.code, "product")
        self.assertEqual(inst.item[0].detail[0].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].detail[0].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].detail[0].unitPrice.value, 100.0)
        self.assertEqual(inst.item[0].detail[1].net.code, "USD")
        self.assertEqual(inst.item[0].detail[1].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].detail[1].net.value, 100.0)
        self.assertEqual(inst.item[0].detail[1].quantity.value, 2)
        self.assertEqual(inst.item[0].detail[1].sequence, 2)
        self.assertEqual(inst.item[0].detail[1].service.code, "lens")
        self.assertEqual(inst.item[0].detail[1].service.system, "http://hl7.org/fhir/ex-visionservice")
        self.assertEqual(inst.item[0].detail[1].type.code, "product")
        self.assertEqual(inst.item[0].detail[1].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].detail[1].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].detail[1].unitPrice.value, 50.0)
        self.assertEqual(inst.item[0].detail[2].factor, 0.07)
        self.assertEqual(inst.item[0].detail[2].net.code, "USD")
        self.assertEqual(inst.item[0].detail[2].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].detail[2].net.value, 14.0)
        self.assertEqual(inst.item[0].detail[2].sequence, 3)
        self.assertEqual(inst.item[0].detail[2].service.code, "fst")
        self.assertEqual(inst.item[0].detail[2].service.system, "http://hl7.org/fhir/ex-visionservice")
        self.assertEqual(inst.item[0].detail[2].type.code, "tax")
        self.assertEqual(inst.item[0].detail[2].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].detail[2].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].detail[2].unitPrice.value, 200.0)
        self.assertEqual(inst.item[0].net.code, "USD")
        self.assertEqual(inst.item[0].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].net.value, 214.0)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(inst.item[0].service.code, "glasses")
        self.assertEqual(inst.item[0].service.system, "http://hl7.org/fhir/ex-visionservice")
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(inst.item[0].type.code, "group")
        self.assertEqual(inst.item[0].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].unitPrice.value, 214.0)
        self.assertEqual(inst.payee.type.code, "provider")
        self.assertEqual(inst.priority.code, "normal")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Vision Claim for Glasses</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "vision")
        self.assertEqual(inst.use, "complete")
    
    def testClaim10(self):
        inst = self.instantiate_from("claim-example-vision.json")
        self.assertIsNotNone(inst, "Must have instantiated a Claim instance")
        self.implClaim10(inst)
        
        js = inst.as_json()
        self.assertEqual("Claim", js["resourceType"])
        inst2 = claim.Claim(js)
        self.implClaim10(inst2)
    
    def implClaim10(self, inst):
        self.assertTrue(inst.coverage[0].focal)
        self.assertEqual(inst.coverage[0].sequence, 1)
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.diagnosis[0].diagnosis.code, "654321")
        self.assertEqual(inst.diagnosis[0].sequence, 1)
        self.assertEqual(inst.id, "660150")
        self.assertEqual(inst.identifier[0].system, "http://happysight.com/claim")
        self.assertEqual(inst.identifier[0].value, "6612345")
        self.assertEqual(inst.item[0].net.code, "USD")
        self.assertEqual(inst.item[0].net.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].net.value, 80.0)
        self.assertEqual(inst.item[0].sequence, 1)
        self.assertEqual(inst.item[0].service.code, "exam")
        self.assertEqual(inst.item[0].service.system, "http://hl7.org/fhir/ex-visionservice")
        self.assertEqual(inst.item[0].servicedDate.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.item[0].servicedDate.as_json(), "2014-08-16")
        self.assertEqual(inst.item[0].type.code, "service")
        self.assertEqual(inst.item[0].unitPrice.code, "USD")
        self.assertEqual(inst.item[0].unitPrice.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].unitPrice.value, 80.0)
        self.assertEqual(inst.payee.type.code, "provider")
        self.assertEqual(inst.priority.code, "normal")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Vision Claim</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "vision")
        self.assertEqual(inst.use, "complete")

