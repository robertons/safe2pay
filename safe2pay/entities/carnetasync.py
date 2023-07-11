# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

class CarnetaSync(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/Carnet'
		cls.__typeRoute__ = 'v2api'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.metadata = Dict()

		super().__init__(**kw)

	def GetCarneta(self, identifier:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}aSync/Get?identifier={identifier}", None, addHeader, typeRoute)
		responseBankSlip = MerchantPaymentResponse(**response)
		return responseBankSlip
	
	def ResendCarneta(self, identifier:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}/Resend?identifier={identifier}", None, addHeader, typeRoute)
		responseBankSlip = MerchantPaymentResponse(**response)
		return responseBankSlip
	
	def CancelCarneta(self, identifier:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Delete(f"{route}/Delete?identifier={identifier}", addHeader, typeRoute)
		responseBankSlip = MerchantPaymentResponse(**response)
		return responseBankSlip