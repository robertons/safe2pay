# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse
from safe2pay.entities.bankslip_response import BankSlipResponse
from safe2pay.entities.marketplacelistresponse import MarketplaceListResponse

class Marketplace(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/Marketplace'
		cls.__typeRoute__ = 'v2api'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.Name = String(max=200)
		cls.CommercialName = String(max=200)
		cls.Identity = String(max=14)
		cls.ResponsibleName = String(max=200)
		cls.ResponsibleIdentity = String(max=11)
		cls.ResponsiblePhone = String(max=11)
		cls.Email = String(max=100)
		cls.TechName = String(max=200)
		cls.TechIdentity = String(max=11)
		cls.TechPhone = String(max=100)
		cls.TechEmail = String(max=100)
		cls.IsPanelRestricted = Boolean()
		cls.BankData = Obj(context=cls, key='BankData', name='BankData')
		cls.Address = Obj(context=cls, key='Address', name='Address')
		cls.MerchantSplit = ObjList(context=cls, key='MerchantSplit', name='MerchantSplit')
		cls.metadata = Dict()

		super().__init__(**kw)

	def CreateSubAccount(self):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Post(f"{route}/Add", self.toJSON(), addHeader, typeRoute)
		marketplace = MerchantPaymentResponse(**response)
		return marketplace
	
	def GetSubAccount(self, idAccount:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response  = Get(f"{route}/Get?id={idAccount}", self.toJSON(), addHeader, typeRoute)
		marketplace = MerchantPaymentResponse(**response)
		return marketplace
	
	def GetList(self, pageNumber:str, rowsPerPage:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response  = Get(f"{route}/List?pageNumber={pageNumber}&rowsPerPage={rowsPerPage}", self.toJSON(), addHeader, typeRoute)
		marketplace = MarketplaceListResponse(**response)
		return marketplace
	
	def PutSubAccount(self, idAccount:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response  = Put(f"{route}/Update?id={idAccount}", self.toJSON(), addHeader, typeRoute)
		marketplace = MerchantPaymentResponse(**response)
		return marketplace
	
	def DeleteSubAccount(self, idAccount:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response  = Delete(f"{route}/Delete?id={idAccount}", addHeader, typeRoute)
		marketplace = MerchantPaymentResponse(**response)
		return marketplace
