# -*- coding: utf-8 -*-
from .lib import *

class ResponseAccountDetail(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}		

		# FIELDS
		cls.ResponseDetail = Obj(context=cls, key='ResponseDetail', name='AccountResponse')
		cls.HasError = Boolean()

		cls.metadata = Dict()

		super().__init__(**kw)
