# -*- coding: utf-8 -*-
# Copyright (c) 2019, Techlift and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

test_records = frappe.get_test_records('Membership Program')


class TestMembershipProgram(unittest.TestCase):
    def test_test(self):
        return True
