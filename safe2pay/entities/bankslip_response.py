# -*- coding: utf-8 -*-
from .lib import *

class BankSlipResponse(Safe2PayEntity):

	def __init__(cls, **kw):

		#cls.__route__ = '/BankSlip'
		#cls.__typeRoute__ = 'v2'
		
		cls.__metadata__ = {}

		# FIELDS
		cls.ResponseDetail = Boolean()
		cls.HasError = Boolean()
		cls.Error = String(max=200)
		cls.Metadata = Dict()

		super().__init__(**kw)