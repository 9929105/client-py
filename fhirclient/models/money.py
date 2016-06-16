#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8522 (http://hl7.org/fhir/StructureDefinition/Money) on 2016-06-16.
#  2016, SMART Health IT.


from . import quantity

class Money(quantity.Quantity):
    """ An amount of economic utility in some recognised currency.
    """
    
    resource_name = "Money"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        super(Money, self).__init__(jsondict=jsondict, strict=strict)


