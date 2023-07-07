# -*- coding: utf-8 -*-
from .lib import *

class MerchantPaymentResponse(Safe2PayEntity):

	def __init__(cls, **kw):
		cls.__metadata__ = {}

		# FIELDS
		cls.HasError = Boolean()
		cls.ResponseDetail = ObjList(context=cls, key='ResponseDetail', name='ResponseDetail')
		
		cls.Error = String(max=200)
		cls.Metadata = Dict()

		super().__init__(**kw)