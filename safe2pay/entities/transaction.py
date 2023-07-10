# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse
from safe2pay.entities.bankslip_response import BankSlipResponse

class Transaction(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/Transaction'
		cls.__typeRoute__ = 'v2api'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.Id = Int()
		#cls.IdTransaction = String(max=26)
		#cls.Status = String(max=26)
		#cls.Message = String(max=26)
		#cls.Application = String(max=26)
		#cls.Vendor = String(max=26)
		cls.Reference = String(max=150)
		cls.CallBackUrl = String(max=150)
		#cls.PaymentDate = String(max=26)
		#cls.PaymentDate = String(max=26)
		#cls.CreatedDate = String(max=26)
		#cls.CreatedDateTime = String(max=26)
		#cls.Amount = String(max=26)
		#cls.NetValue = String(max=26)
		#cls.DiscountAmount = String(max=26)
		#cls.TaxValue = String(max=26)
		#cls.PaymentMethod = String(max=26)
		#cls.Customer = String(max=26)
		#cls.Products = String(max=26)
		#cls.AmountPayment = String(max=26)
		#cls.CheckingAccounts = String(max=26)
		#cls.PaymentObject = String(max=26)
		cls.Metadata = Dict()

		super().__init__(**kw)

	def UpdateTransaction(self, isUpdateReference:bool, isUpdateCallBackUrl:bool):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Put(f"{route}/Update?isUpdateReference={isUpdateReference}&isUpdateCallBackUrl={isUpdateCallBackUrl}", self.toJSON(), addHeader, typeRoute)
		transacao = MerchantPaymentResponse(**response)
		return transacao
	
	def UpdateSandboxTransaction(self, idTransaction:Int, idTransactionStatus:Int):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Put(f"{route}/UpdateSandboxTransaction?idTransaction={idTransaction}&idTransactionStatus={idTransactionStatus}", None, addHeader, typeRoute)
		transacao = BankSlipResponse(**response)
		return transacao
	
	def GetTransaction(self, id:int):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}/Get?Id={id}", None, addHeader, typeRoute)
		transacao = MerchantPaymentResponse(**response)
		return transacao
