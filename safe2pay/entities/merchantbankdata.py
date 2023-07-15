# -*- coding: utf-8 -*-
from .lib import *

from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

class MerchantBankData(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		cls.__route__ = '/MerchantBankData'
		cls.__typeRoute__ = 'v2api'

		# FIELDS
		cls.id = String(max=26)
		cls.Identity = String(max=20)
		cls.Name = String(max=150)
		cls.MerchantType = Obj(context=cls, key='MerchantType', name='MerchantType')
		cls.BankData = Obj(context=cls, key='BankData', name='BankData')
		cls.metadata = Dict()

		super().__init__(**kw)

	def GetMerchantBankData(self):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}/Get", None, addHeader, typeRoute)
		return MerchantPaymentResponse(**response)
