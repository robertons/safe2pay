# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.bankslip_response import BankSlipResponse
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse
from safe2pay.entities.transaction_response import TransactionResponse

class Plan(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/Plans'
		cls.__typeRoute__ = 'v1'
		cls.__module__ = 'Recurrence'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.PlanOption = Int()
		cls.PlanFrequence = Int()
		cls.ChargeDay = Int()
		cls.DayOfWeek = Int()
		cls.Name = String(max=200)
		cls.Description = String(max=100)
		cls.Amount = DecimalS2P(max=15)
		cls.SubscriptionTax = DecimalS2P(max=15)
		cls.SubscriptionLimit = Int()
		cls.IsImmediateCharge = Boolean()
		cls.IsProRata = Boolean()
		cls.DaysBeforeChargeDateExpiration = Int()
		cls.DaysBeforeCancel = Int()
		cls.BillingCycle = Int()
		cls.CallbackUrl = String(max=2000)
		cls.DaysDue = Int()
		cls.Instruction = String(max=2000)
		cls.Message = String(max=200)
		cls.PenaltyAmount = DecimalS2P(max=15)
		cls.InterestAmount = DecimalS2P(max=15)
		cls.DiscountType = Int()
		cls.DiscountDue = DateTime(format="%d/%m/%Y")
		cls.DiscountAmount = DecimalS2P(max=15)

		super().__init__(**kw)

	def CreatePlan(self):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		print("ROUTE")
		print(route)
		response = Post(f"{route}", self.toJSON(), addHeader, typeRoute, self.__module__)
		newPlan = MerchantPaymentResponse(**response)
		return newPlan
	
	def GetPlan(self, id:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}/{id}", None, addHeader, typeRoute, self.__module__)
		plan = MerchantPaymentResponse(**response)
		return plan
	
	def ListPlans(self, name:str, isEnabled:str, pageNumber:str, rowsPerPage:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})

		urlCompleta = f"{route}?"

		if name != None:
			urlCompleta = urlCompleta + f"name={name}&"

		if isEnabled != None:
			urlCompleta = urlCompleta + f"isEnabled={isEnabled}&"

		if pageNumber != None:
			urlCompleta = urlCompleta + f"PageNumber={pageNumber}&"

		if rowsPerPage != None:
			urlCompleta = urlCompleta + f"RowsPerPage={rowsPerPage}&"
			
		response = Get(f"{urlCompleta}",None, addHeader, typeRoute, self.__module__)
		transacoes = TransactionResponse(**response)
		return transacoes
	
	def DisablePlan(self, id:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Patch(f"{route}/{id}/Disable", None, addHeader, typeRoute, self.__module__)
		plan = MerchantPaymentResponse(**response)
		return plan
	