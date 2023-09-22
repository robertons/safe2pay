# -*- coding: utf-8 -*-
from .lib import *

class PlanSubscriptionCancelResponse(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.success = Boolean()
		cls.StatusCode = Int()
		cls.Errors = ObjList(context=cls, key='Errors', name='ErroResponse')

		cls.metadata = Dict()

		super().__init__(**kw)