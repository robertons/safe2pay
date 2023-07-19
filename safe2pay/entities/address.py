# -*- coding: utf-8 -*-
from .lib import *

class Address(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.ZipCode = String(max=8)
		cls.Street = String(max=150)
		cls.Number = String(max=15)
		cls.District = String(max=60)
		cls.CityName = String(max=200)
		cls.City = Obj(context=cls, key='City', name='City')
		cls.StateInitials = String(max=2)
		cls.State = String(max=100)
		cls.Complement = String(max=150)
		cls.CountryName = String(max=200)
		cls.metadata = Dict()

		super().__init__(**kw)
