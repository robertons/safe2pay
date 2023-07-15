# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.bankslip_response import BankSlipResponse

class BankSlip(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/BankSlip'
		cls.__typeRoute__ = 'v2api'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.metadata = Dict()
		cls.Amount = DecimalS2P(max=18)
		cls.DueDate = DateTime(format="%d/%m/%Y")
		cls.Message = ObjList(context=cls, key='Message', name='str')
		cls.DiscountAmount = DecimalS2P(max=18)
		cls.DiscountType = Int()
		cls.DiscountDue = DateTime(format="%d/%m/%Y")

		super().__init__(**kw)

	def ReleaseBankSlip(self, idTransaction:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}/ReleaseBankSlip?idTransaction={idTransaction}", None, addHeader, typeRoute)
		responseBankSlip = BankSlipResponse(**response)
		return responseBankSlip
	
	def WriteOffBankSlip(self, idTransaction:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Delete(f"{route}/WriteOffBankSlip?idTransaction={idTransaction}", addHeader, typeRoute)
		responseBankSlip = BankSlipResponse(**response)
		return responseBankSlip