# -*- coding: utf-8 -*-
# Copyright (c) 2021, it126 and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LibraryMembership(Document):
	def before_submit(self):
		exists = frappe.db.exists(
			'Library Membership',
			{
				'library_member': self.library_member,
				'docstatus': 1,
				'to_date': (">", self.from_date),
			},
		)
		if exists:
			frappe.throw("There is an active member for this member")

		loan_period = frappe.db.get_sing_value("Library Setting", "loan_period")
		self.todate = frappe.utils.add_days(self.from_date, load_period or 30)