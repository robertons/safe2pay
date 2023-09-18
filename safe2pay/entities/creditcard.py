# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.bankslip_response import BankSlipResponse
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

class CreditCard(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}	
		cls.__route__ = '/CreditCard'
		cls.__typeRoute__ = 'v2api'	

		# FIELDS
		cls.id = String(max=26)
		cls.Holder = String(max=25)
		cls.CardNumber = String(max=19)
		cls.ExpirationDate = String(max=7)
		cls.SecurityCode = String(max=4)
		cls.Token = String(max=42)
		cls.Brand = Int()
		cls.Installments = Int()
		cls.metadata = Dict()

		super().__init__(**kw)

	# Transações de cartão de crédito que contenham split de pagamento ficarão indisponíveis para estorno parcial.
	def CancelCredit(self, idTransaction:str, amount:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Delete(f"{route}/Cancel/{idTransaction}/{amount}", addHeader, typeRoute)
		payment = MerchantPaymentResponse(**response)
		return payment
	
	def CaptureCredit(self, idTransaction:str, amount:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Put(f"{route}/Capture/{idTransaction}/{amount}", None, addHeader, typeRoute)
		payment = MerchantPaymentResponse(**response)
		return payment

