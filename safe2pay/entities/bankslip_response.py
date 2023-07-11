# -*- coding: utf-8 -*-
from .lib import *

class BankSlipResponse(Safe2PayEntity):

	def __init__(cls, **kw):
		
		cls.__metadata__ = {}

		# FIELDS
		cls.ResponseDetail = Boolean()
		cls.HasError = Boolean()
		cls.ErrorCode = String(max=10)
		cls.Error = String(max=200)
		cls.Metadata = Dict()

		super().__init__(**kw)