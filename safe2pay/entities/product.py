# -*- coding: utf-8 -*-
from .lib import *

class Product(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.Code = String(max=50)
		cls.Description = String(max=200)
		cls.UnitPrice = Decimal(max=18, scale=2)
		cls.Quantity = Decimal(max=18, scale=2)
		cls.metadata = Dict()

		super().__init__(**kw)
