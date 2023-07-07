# -*- coding: utf-8 -*-
from .lib import *

class StaticPix(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/StaticPix'
		cls.__typeRoute__ = 'v2'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.Ammount = Decimal()
		cls.Description = String(max=30)
		cls.Reference = String(max=60)
		cls.CallbackUrl = String(max=200)
		cls.metadata = Dict()

		super().__init__(**kw)
