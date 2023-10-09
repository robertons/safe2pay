# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse
from safe2pay.entities.bankslip_response import BankSlipResponse
from safe2pay.entities.transaction_response import TransactionResponse
from safe2pay.entities.transactiongetresponse import TransactionGetResponse

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
		transacao = TransactionGetResponse(**response)
		return transacao
	
	def GetTransactionByReference(self, reference:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}/Reference?reference={reference}", None, addHeader, typeRoute)
		transacao = MerchantPaymentResponse(**response)
		return transacao
	
	def GetTransactionList(self, pageNumber:str, rowsPerPage:str, createdDateInitial:str, createdDateEnd:str, paymentDateInitial:str, paymentDateEnd:str, amountInitial:str, amountEnd:str, objId:int, objReference:str, objApplication:str, objVendor:str, objCustomerName:str, objCustomerIdentity:str, objPaymentCode:str, objTransactionStatus:str, objIsSandbox:bool):
		addHeader, route, typeRoute = self.FormatRoute(**{})

		urlCompleta = f"{route}/List?"

		if pageNumber != None:
			urlCompleta = urlCompleta + f"PageNumber={pageNumber}&"

		if rowsPerPage != None:
			urlCompleta = urlCompleta + f"RowsPerPage={rowsPerPage}&"

		if createdDateInitial != None:
			urlCompleta = urlCompleta + f"CreatedDateInitial={createdDateInitial}&"

		if createdDateEnd != None:
			urlCompleta = urlCompleta + f"CreatedDateEnd={createdDateEnd}&"

		if paymentDateInitial != None:
			urlCompleta = urlCompleta + f"PaymentDateInitial={paymentDateInitial}&"

		if paymentDateEnd != None:
			urlCompleta = urlCompleta + f"PaymentDateEnd={paymentDateEnd}&"

		if amountInitial != None:
			urlCompleta = urlCompleta + f"AmountInitial={amountInitial}&"

		if amountEnd != None:
			urlCompleta = urlCompleta + f"AmountEnd={amountEnd}&"

		if objId != None:
			urlCompleta = urlCompleta + f"Object.Id={objId}&"

		if objReference != None:
			urlCompleta = urlCompleta + f"Object.Reference={objReference}&"

		if objApplication != None:
			urlCompleta = urlCompleta + f"Object.Application={objApplication}&"

		if objVendor != None:
			urlCompleta = urlCompleta + f"Object.Vendor={objVendor}&"

		if objCustomerName != None:
			urlCompleta = urlCompleta + f"Object.Customer.Name={objCustomerName}&"

		if objCustomerIdentity != None:
			urlCompleta = urlCompleta + f"Object.Customer.Identity={objCustomerIdentity}&"

		if objPaymentCode != None:
			urlCompleta = urlCompleta + f"Object.PaymentMethod.Code={objPaymentCode}&"

		if objTransactionStatus != None:
			urlCompleta = urlCompleta + f"Object.TransactionStatus.Code={objTransactionStatus}&"

		if objIsSandbox != None:
			urlCompleta = urlCompleta + f"Object.IsSandbox={objIsSandbox}&"
			
		response = Get(f"{urlCompleta}",None, addHeader, typeRoute)
		transacoes = TransactionResponse(**response)
		return transacoes


