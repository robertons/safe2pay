# -*- coding: utf-8 -*-
from .lib import *

class TransactionListResponse(Safe2PayEntity):

	def __init__(cls, **kw):
		cls.__metadata__ = {}

		# FIELDS
		cls.TotalItems = Int()
		cls.Objects = ObjList(context=cls, key='ResponseDetail', name='ResponseDetail')
		cls.Objects1 = ObjList(context=cls, key='Objects', name='ResponseDetail')
		
		cls.Error = String(max=200)
		cls.Metadata = Dict()

		super().__init__(**kw)