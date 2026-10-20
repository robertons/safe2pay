# -*- coding: utf-8 -*-
from .lib import *

class Phone(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.country_code = Int()
		cls.area_code = Int()
		cls.number = Int()


		super().__init__(**kw)
