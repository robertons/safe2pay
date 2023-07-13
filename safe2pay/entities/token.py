# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse
from safe2pay.entities.bankslip_response import BankSlipResponse

class Token(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/Token'
		cls.__typeRoute__ = 'v2'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.IsSandbox = Boolean()
		cls.Holder = String(max=25)
		cls.CardNumber = String(max=19)
		cls.ExpirationDate = DateTime(format="%m/%Y")
		cls.SecurityCode = String(max=4)
		cls.metadata = Dict()

		super().__init__(**kw)

	def CreateToken(self):
		self.__typeRoute__ = 'v2'
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Post(f"{route}", self.toJSON(), addHeader, typeRoute)
		token = MerchantPaymentResponse(**response)
		return token
	
	def DeleteToken(self, cardToken:str):
		self.__typeRoute__ = 'v2api'
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response  = Delete(f"{route}/delete?cardToken={cardToken}", addHeader, typeRoute)
		token = BankSlipResponse(**response)
		return token
