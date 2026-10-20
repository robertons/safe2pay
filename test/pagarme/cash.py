# -*- coding: utf-8 -*-
from .lib import *

class Cash(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.description = String(max=256)
		cls.confirm = Boolean()
		cls.metadata = Dict()


		super().__init__(**kw)
