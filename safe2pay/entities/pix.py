# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.bankslip_response import BankSlipResponse

class Pix(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/Pix'
		cls.__typeRoute__ = 'v2api'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.Id = Int()
	
		cls.metadata = Dict()

		super().__init__(**kw)

	def CancelPix(self, idTransaction:str):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Delete(f"{route}/Cancel/{idTransaction}", addHeader, typeRoute)
		payment = BankSlipResponse(**response)
		return payment