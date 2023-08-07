# -*- coding: utf-8 -*-
from .lib import *

class ErroResponse(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.ErrorName = String(max=500)
		cls.Message = String(max=500)

		cls.metadata = Dict()

		super().__init__(**kw)