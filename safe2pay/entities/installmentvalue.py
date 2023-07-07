# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

class InstallmentValue(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/CreditCard'
		cls.__typeRoute__ = 'v2api'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.metadata = Dict()

		super().__init__(**kw)

	def GetInstallmentValues(self, amount:decimal):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}/InstallmentValue?amount={amount}", None, addHeader, typeRoute)
		responseBankSlip = MerchantPaymentResponse(**response)
		return responseBankSlip
