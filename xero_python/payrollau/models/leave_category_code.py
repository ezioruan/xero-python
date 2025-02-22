# coding: utf-8

"""
    Xero Payroll AU API

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from enum import Enum


class LeaveCategoryCode(Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    allowed enum values
    """

    ANNUALLEAVE = "ANNUALLEAVE"
    LONGSERVICELEAVE = "LONGSERVICELEAVE"
    PERSONALCARERSLEAVE = "PERSONALCARERSLEAVE"
    ROSTEREDDAYOFF = "ROSTEREDDAYOFF"
    TIMEOFFINLIEU = "TIMEOFFINLIEU"
    COMPASSIONATEANDBEREAVEMENTLEAVE = "COMPASSIONATEANDBEREAVEMENTLEAVE"
    STUDYLEAVE = "STUDYLEAVE"
    FAMILYANDDOMESTICVIOLENCELEAVE = "FAMILYANDDOMESTICVIOLENCELEAVE"
    SPECIALPAIDLEAVE = "SPECIALPAIDLEAVE"
    COMMUNITYSERVICELEAVE = "COMMUNITYSERVICELEAVE"
    JURYDUTYLEAVE = "JURYDUTYLEAVE"
    DEFENCERESERVELEAVE = "DEFENCERESERVELEAVE"
