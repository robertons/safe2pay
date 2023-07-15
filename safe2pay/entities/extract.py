# -*- coding: utf-8 -*-
from .lib import *

class Extract(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.IdTransaction = Int()
		cls.metadata = Dict()

		super().__init__(**kw)
