# -*- coding: utf-8 -*-
from .lib import *

class TransactionGetResponse(Safe2PayEntity):

	def __init__(cls, **kw):
		cls.__metadata__ = {}

		# FIELDS
		cls.HasError = Boolean()
		cls.Error = String(max=200)
		cls.ErrorCode = String(max=10)

		cls.Success = Boolean()

		cls.ResponseDetail = ObjList(context=cls, key='ResponseDetail', name='ResponseDetailTransactionGet')
		cls.Metadata = Dict()

		super().__init__(**kw)