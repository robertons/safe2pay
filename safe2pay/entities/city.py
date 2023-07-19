# -*- coding: utf-8 -*-
from .lib import *

class City(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.CodeIBGE = String(max=20)
		cls.metadata = Dict()

		super().__init__(**kw)
