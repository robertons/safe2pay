# -*- coding: utf-8 -*-
from .lib import *

class TransactionResponse(Safe2PayEntity):

	def __init__(cls, **kw):
		cls.__metadata__ = {}

		# FIELDS
		cls.HasError = Boolean()
		cls.ResponseDetail = Obj(context=cls, key='TransactionListResponse', name='TransactionListResponse')
		cls.ResponseDetail1 = Obj(context=cls, key='ResponseDetail', name='TransactionListResponse')
		
		cls.Error = String(max=200)
		cls.Metadata = Dict()

		super().__init__(**kw)