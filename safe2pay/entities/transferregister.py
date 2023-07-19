# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse
from safe2pay.entities.bankslip_response import BankSlipResponse
from safe2pay.entities.transactionlistresponse import TransactionListResponse

class TransferRegister(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/Transfer'
		cls.__typeRoute__ = 'v2'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.BankData = ObjList(context=cls, key='BankData', name='BankData')
		cls.ReceiverName = String(max=200)
		cls.Identity = String(max=14)
		cls.Identification = String(max=100)
		cls.Amount = DecimalS2P(max=15)
		cls.CompensationDate = DateTime(format="%Y-%m-%d")
		cls.CallbackUrl = String(max=200)
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
	
	def GetTransfer(self, idTransferRegister:str):
		self.__typeRoute__ = 'v2api'
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response  = Get(f"{route}/Get?Id={idTransferRegister}", self.toJSON(), addHeader, typeRoute)

		print("RESPONSE")
		print(response)
		transfer = MerchantPaymentResponse(**response)
		return transfer
	
	def ListTransfers(self, pageNumber:str, rowsPerPage:str):
		self.__typeRoute__ = 'v2api'
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response  = Get(f"{route}/ListLot?pageNumber={pageNumber}&rowsPerPage={rowsPerPage}", self.toJSON(), addHeader, typeRoute)

		transfer = TransactionListResponse(**response['ResponseDetail'])
		return transfer
	
	def ListLotTransfers(self, idTransferRegisterLot:str, pageNumber: str, rowsPerPage:str):
		self.__typeRoute__ = 'v2api'
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response  = Get(f"{route}/List?Object.IdTransferRegisterLot={idTransferRegisterLot}&pageNumber={pageNumber}&rowsPerPage={rowsPerPage}", self.toJSON(), addHeader, typeRoute)

		transfer = TransactionListResponse(**response['ResponseDetail'])
		return transfer