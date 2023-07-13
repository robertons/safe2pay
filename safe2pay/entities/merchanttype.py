# -*- coding: utf-8 -*-
from .lib import *

class MerchantType(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.Code = String(max=3)
		cls.Name = String(max=50)
		cls.metadata = Dict()

		super().__init__(**kw)
