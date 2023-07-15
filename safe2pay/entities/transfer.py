# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse
from safe2pay.entities.bankslip_response import BankSlipResponse

class Transfer(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/Transfer'
		cls.__typeRoute__ = 'v2'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.TransferRegisters = ObjList(context=cls, key='TransferRegisters', name='TransferRegister')
		cls.metadata = Dict()

		super().__init__(**kw)

	def PostTransfer(self):
		self.__typeRoute__ = 'v2'
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Post(f"{route}", self.toJSON(), addHeader, typeRoute)
		token = MerchantPaymentResponse(**response)
		return token
	
