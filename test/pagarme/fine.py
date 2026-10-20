# -*- coding: utf-8 -*-
from .lib import *

class Fine(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.days = Int()
		cls.type = String(max=20)
		cls.amount = Int()

		super().__init__(**kw)
