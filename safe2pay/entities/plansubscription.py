# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.bankslip_response import BankSlipResponse
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse
from safe2pay.entities.transaction_response import TransactionResponse
from safe2pay.entities.planresponse import PlanResponse
from safe2pay.entities.responsedetail import ResponseDetail
from safe2pay.entities.plansubscriptioncancelresponse import PlanSubscriptionCancelResponse

class PlanSubscription(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/Subscriptions'
		cls.__typeRoute__ = 'v1'
		cls.__module__ = 'Recurrence'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.Plan = Obj(context=cls, key='Plan', name='Plan')
		cls.Token = String(max=50)
		cls.SubscriptionDate = DateTime(format="%Y-%m-%d")
		cls.PaymentMethod = Int()

		super().__init__(**kw)

	def CreatePlanSimulate(self):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Post(f"{route}/Simulate", self.toJSON(), addHeader, typeRoute, self.__module__)
		newPlan = PlanResponse(**response)
		return newPlan
	
	def GetSubscription(self, idSubscription:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}/{idSubscription}", self.toJSON(), addHeader, typeRoute, self.__module__)
		newPlan = PlanResponse(**response)
		return newPlan
	
	def ListSubscriptions(self, pageNumber:str, rowsPerPage:str, customerName:str, status:str, initialDate:str, endDate:str, idPlan:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})

		urlCompleta = f"{route}?"

		if pageNumber != None:
			urlCompleta = urlCompleta + f"PageNumber={pageNumber}&"

		if rowsPerPage != None:
			urlCompleta = urlCompleta + f"RowsPerPage={rowsPerPage}&"

		if customerName != None:
			urlCompleta = urlCompleta + f"CustomerName={customerName}&"

		if status != None:
			urlCompleta = urlCompleta + f"Status={status}&"

		if initialDate != None:
			urlCompleta = urlCompleta + f"InitialDate={initialDate}&"

		if endDate != None:
			urlCompleta = urlCompleta + f"EndDate={endDate}&"

		if idPlan != None:
			urlCompleta = urlCompleta + f"IdPlan={idPlan}&"
			
		response = Get(f"{urlCompleta}",None, addHeader, typeRoute, self.__module__)
		subscriptions = PlanResponse(**response)
		return subscriptions
	
	def GetSubscriptionCharges(self, idSubscription:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}/{idSubscription}/Charges", self.toJSON(), addHeader, typeRoute, self.__module__)
		charges = PlanResponse(**response)
		return charges
	
	def DisableSubscription(self, idSubscription:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Patch(f"{route}/{idSubscription}/Disable", self.toJSON(), addHeader, typeRoute, self.__module__)

		if (response != None):
			subscription = PlanSubscriptionCancelResponse(**response)
			return subscription
		
		return response
	
	def UpdateTokenCard(self, idSubscription:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Patch(f"{route}/{idSubscription}/UpdateTokenCard", self.toJSON(), addHeader, typeRoute, self.__module__)
		subscription = PlanResponse(**response)
		return subscription