# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.bankslip_response import BankSlipResponse
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

class MerchantPaymentDate(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/MerchantPaymentDate'
		cls.__typeRoute__ = 'v2api'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.metadata = Dict()
		cls.PlanFrequence = ObjList(context=cls, key='PlanFrequence', name='PlanFrequence')
		cls.PaymentDay = Int()

		super().__init__(**kw)

	def Update(self):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Put(f"{route}/Update", self.toJSON(), addHeader, typeRoute)
		print("RESPONSE")
		print(response)
		antecipacao = BankSlipResponse(**response)
		return antecipacao