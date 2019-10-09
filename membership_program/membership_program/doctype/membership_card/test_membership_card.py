# -*- coding: utf-8 -*-
# Copyright (c) 2019, Techlift and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

test_records = frappe.get_test_records('Membership Card')

class TestMembershipCard(unittest.TestCase):
    def test_card_cost(self):
        return True
