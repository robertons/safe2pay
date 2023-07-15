# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.bankslip_response import BankSlipResponse
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

class Anticipation(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/Anticipation'
		cls.__typeRoute__ = 'v2api'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.metadata = Dict()
		cls.PaymentStartDate = DateTime(format="%Y-%m-%d")
		cls.PaymentEndDate = DateTime(format="%Y-%m-%d")
		cls.SessionGuid = String(max=50)
		cls.EffectivenessList = ObjList(context=cls, key='EffectivenessList', name='Effectiveness')

		super().__init__(**kw)

	def Simulate(self):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Post(f"{route}/Simulate", self.toJSON(), addHeader, typeRoute)
		print("RESPONSE")
		print(response)
		antecipacao = MerchantPaymentResponse(**response)
		return antecipacao
	
	def EffectSimulate(self):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Post(f"{route}/EffectSimulate", self.toJSON(), addHeader, typeRoute)
		print("RESPONSE")
		print(response)
		antecipacao = MerchantPaymentResponse(**response)
		return antecipacao