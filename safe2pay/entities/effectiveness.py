# -*- coding: utf-8 -*-
from .lib import *

class Effectiveness(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.ReleaseDate = DateTime(format="%Y-%m-%d")

		super().__init__(**kw)
