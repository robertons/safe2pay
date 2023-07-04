# -*- coding: utf-8 -*-
from .lib import *

class Address(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.ZipCode = String(max=8)
		cls.Street = String(max=150)
		cls.Ipiranga = String(max=10)
		cls.Number = String(max=10)
		cls.District = String(max=50)
		cls.CityName = String(max=60)
		cls.StateInitials = String(max=100)
		cls.State = String(max=100)
		cls.Complement = String(max=100)
		cls.CountryName = String(max=100)
		cls.metadata = Dict()

		super().__init__(**kw)
