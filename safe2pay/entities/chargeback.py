# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.bankslip_response import BankSlipResponse
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

class Chargeback(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/Chargeback'
		cls.__typeRoute__ = 'v2api'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.metadata = Dict()

		super().__init__(**kw)

	def ListChargebacks(self, pageNumber:str, rowsPerPage:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})

		urlCompleta = f"{route}/List?"

		if pageNumber != None:
			urlCompleta = urlCompleta + f"PageNumber={pageNumber}&"

		if rowsPerPage != None:
			urlCompleta = urlCompleta + f"RowsPerPage={rowsPerPage}&"
			
		response = Get(f"{urlCompleta}",None, addHeader, typeRoute, self.__module__)

		chargebacks = MerchantPaymentResponse(**response)
		return chargebacks
	
	def GetChargeback(self, idChargeback:str, idTransaction:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}/Get?Id={idChargeback}&IdTransaction={idTransaction}",None, addHeader, typeRoute, self.__module__)

		chargebacks = MerchantPaymentResponse(**response)
		return chargebacks