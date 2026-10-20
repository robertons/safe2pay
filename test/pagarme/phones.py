# -*- coding: utf-8 -*-
from .lib import *

class Phones(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.home_phone = Obj(context=cls, key='home_phone', name='Phone')
		cls.mobile_phone = Obj(context=cls, key='mobile_phone', name='Phone')
		
		super().__init__(**kw)
