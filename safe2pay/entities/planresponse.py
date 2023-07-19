# -*- coding: utf-8 -*-
from .lib import *

class PlanResponse(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.success = Boolean()
		cls.data = Obj(context=cls, key='Data', name='PlanDataResponse')

		cls.metadata = Dict()

		super().__init__(**kw)