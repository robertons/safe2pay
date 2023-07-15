# -*- coding: utf-8 -*-
from .lib import *

from safe2pay.entities.responsedetail_account import ResponseAccountDetail

from safe2pay.entities.deposit import Deposit
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

class CheckingAccount(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}
		cls.__route__ = '/CheckingAccount'
		cls.__typeRoute__ = 'v2api'

		# FIELDS
		cls.id = String(max=26)
		cls.Description = String(max=100)
		cls.Amount = DecimalS2P(max=18)
		cls.Tax = DecimalS2P(max=18)
		cls.IsTransferred = Boolean()
		cls.ReleaseDate = DateTime(format="%Y-%m-%d")
		cls.InstallmentNumber = Int()
		cls.metadata = Dict()

		super().__init__(**kw)

	def ListDeposits(self, month:str, year:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}/GetListDeposits?month={month}&year={year}", None, addHeader, typeRoute)
		respAccountDetail = ResponseAccountDetail(**response)
		return respAccountDetail
	
	def DetailDeposits(self, day:str, month:str, year:str, page:str, rowsPerPage:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}/GetListDetailsDeposits?day={day}&month={month}&year={year}&page={page}&rowPerPage={rowsPerPage}", None, addHeader, typeRoute)
		deposits = Deposit(**response['ResponseDetail'])
		return deposits
	
	def GetBalance(self, initialDate:str, endDate:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Get(f"{route}/GetBalance?initialDate={initialDate}&endDate={endDate}", None, addHeader, typeRoute)
		balance = MerchantPaymentResponse(**response)
		return balance
	