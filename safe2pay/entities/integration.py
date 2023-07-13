# -*- coding: utf-8 -*-
from .lib import *

class Integration(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.Token = String(max=100)
		cls.TokenSandbox = String(max=100)
		cls.SecretKey = String(max=100)
		cls.SecretKeySandbox = String(max=100)
		cls.metadata = Dict()

		super().__init__(**kw)
