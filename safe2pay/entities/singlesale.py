# -*- coding: utf-8 -*-
from .lib import *

from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse
from safe2pay.entities.bankslip_response import BankSlipResponse
from safe2pay.entities.transaction_response import TransactionResponse
class SingleSale(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}	
		cls.__route__ = '/SingleSale'
		cls.__typeRoute__ = 'v2api'	

		# FIELDS
		cls.id = String(max=26)
		cls.DueDate = DateTime(format="%Y-%m-%d")
		cls.ExpirationDate = DateTime(format="%Y-%m-%d")
		cls.DiscountAmount = DecimalS2P(max=13)
		cls.DiscountType = Int()
		cls.CallbackUrl = String(max=200)
		cls.Instruction = String(max=200)
		cls.Emails = ObjList(context=cls, key='Emails', name='str')
		cls.Messages = ObjList(context=cls, key='Messages', name='str')
		cls.PenaltyAmount = DecimalS2P(max=13)
		cls.InsterestAmount = DecimalS2P(max=13)
		cls.InstallmentQuantity = Int()
		cls.Reference = String(max=60)
		cls.Splits = ObjList(context=cls, key='Splits', name='Split');
		cls.Customer = ObjList(context=cls, key='Customer', name='Customer')
		cls.Products = ObjList(context=cls, key='Products', name='Product')
		cls.PaymentsMethods = ObjList(context=cls, key='PaymentMethods', name='PaymentMethod')
		cls.metadata = Dict()

		super().__init__(**kw)
		
    
	def CreateSingleSale(self):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Post(f"{route}/Add", self.toJSON(), addHeader, typeRoute)
		singleSale = MerchantPaymentResponse(**response)
		return singleSale
	
	def GetSingleSale(self, singleSaleHash:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}/Get?singleSaleHash={singleSaleHash}", self.toJSON(), addHeader, typeRoute)
		singleSale = MerchantPaymentResponse(**response)
		return singleSale
	
	def ResendSingleSale(self, singleSaleHash:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}/Resend?singleSaleHash={singleSaleHash}", self.toJSON(), addHeader, typeRoute)
		singleSale = BankSlipResponse(**response)
		return singleSale
	
	def CancelSingleSale(self, singleSaleHash:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Delete(f"{route}/Delete?singleSaleHash={singleSaleHash}", addHeader, typeRoute)
		singleSale = BankSlipResponse(**response)
		return singleSale
	
	def ListSingleSales(self, pageNumber:str, rowsPerPage:str, createdDateInitial:str, createdDateEnd:str, objReference:str, objCustomerName:str, objCustomerIdentity:str, objTransactionStatus:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})

		urlCompleta = f"{route}/List?"

		if pageNumber != None:
			urlCompleta = urlCompleta + f"PageNumber={pageNumber}&"

		if rowsPerPage != None:
			urlCompleta = urlCompleta + f"RowsPerPage={rowsPerPage}&"

		if createdDateInitial != None:
			urlCompleta = urlCompleta + f"InitialDate={createdDateInitial}&"

		if createdDateEnd != None:
			urlCompleta = urlCompleta + f"EndDate={createdDateEnd}&"

		if objReference != None:
			urlCompleta = urlCompleta + f"Object.Reference={objReference}&"

		if objCustomerName != None:
			urlCompleta = urlCompleta + f"Object.Customer.Name={objCustomerName}&"

		if objCustomerIdentity != None:
			urlCompleta = urlCompleta + f"Object.Customer.Identity={objCustomerIdentity}&"

		if objTransactionStatus != None:
			urlCompleta = urlCompleta + f"Object.TransactionStatus.Code={objTransactionStatus}&"
			
		response = Get(f"{urlCompleta}",None, addHeader, typeRoute)
		transacoes = TransactionResponse(**response)
		return transacoes
	