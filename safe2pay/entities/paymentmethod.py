# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

class PaymentMethod(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}
		cls.__route__ = '/PaymentMethod'
		cls.__typeRoute__ = 'v2api'

		# FIELDS
		cls.Id = String(max=26)
		cls.Code = String(max=26)
		cls.CodePaymentMethod = String(max=26)
		cls.Name = String(max=26)
		cls.PaymentMethod = Int()
		cls.IsPayTax = Boolean()
		cls.Amount = DecimalS2P(max=15)
		cls.Tax = DecimalS2P(max=15)
		cls.Description = String(max=100)
		cls.Reference = String(max=100)
		cls.InstallmentCurrent = Int()
		cls.InstallmentQuantity = Int()
		cls.Taxes = ObjList(context=cls, key='Tax', name='Tax')
		
		super().__init__(**kw)

	def ListPaymentMethods(self):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}/List",None, addHeader, typeRoute, self.__module__)

		#paymentMethods = MerchantPaymentResponse(**response)
		return response

	def GetPaymentMethod(self, code:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}/Get?codePaymentMethod={code}",None, addHeader, typeRoute, self.__module__)

		#paymentMethods = MerchantPaymentResponse(**response)
		return response