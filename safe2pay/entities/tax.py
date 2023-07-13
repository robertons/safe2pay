# -*- coding: utf-8 -*-
from .lib import *

class Tax(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.TaxTypeName = String(max=1)
		cls.TaxType = String(max=1)
		cls.Tax = DecimalS2P(max=3)
		cls.metadata = Dict()

		super().__init__(**kw)
