# -*- coding: utf-8 -*-
# Copyright (c) 2019, Techlift and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class MembershipCard(Document):
	def validate(self):

		"""Field Validations"""
		if self.card_cost and not self.card_code < 0:
			frappe.throw(_("Card Cost should be greater than 0"))

		if self.valid_for and not self.valid_for < 1:
			frappe.throw(_("Valid for should be greater than or equal to 1 month"))

		if self.maximum_members_allowed and not self.maximum_members_allowed < 1:
			frappe.throw(_("Maximum Members Allowed should be greater than or equal to 1 member"))

		if self.discount and not (self.discount > 100 or self.discount < 0):
			frappe.throw(_("Discount should be in between 0% and 100%"))

	pass
