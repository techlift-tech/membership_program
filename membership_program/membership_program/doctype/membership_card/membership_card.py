# -*- coding: utf-8 -*-
# Copyright (c) 2019, Techlift and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document


class MembershipCard(Document):
    def validate(self):
        """Field Validations"""
        if self.card_cost and self.card_cost < 0:
            frappe.throw(_("Card Cost should be greater than 0"))

        if self.valid_for and self.valid_for < 1:
            frappe.throw(_("Valid for should be greater than or equal to 1 month"))

        if self.maximum_members_allowed and self.maximum_members_allowed < 1:
            frappe.throw(_("Maximum Members Allowed should be greater than or equal to 1 member"))

        if self.discount and (self.discount > 100 or self.discount < 0):
            frappe.throw(_("Discount should be in between 0% and 100%"))

        if self.item_groups:
            for item_group in self.item_groups:
                if item_group.discount > 100 or item_group.discount < 0:
                    frappe.throw(_("Item Group Discount should be in between 0% and 100%"))

        if self.items:
            for item in self.items:
                if item.discount > 100 or item.discount < 0:
                    frappe.throw(_("Item Discount should be in between 0% and 100%"))

        # Check it item group is present both in Inclusive and Exclusive
        if self.common_elements_in_lists(self.item_groups, self.ex_item_groups, "item_group"):
            frappe.throw(_("Same Groups cannot be both Included and Excluded"))

        # Check if item is present both in Inclusive and Exclusive
        if self.common_elements_in_lists(self.items, self.ex_item, "item"):
            frappe.throw(_("Same Groups cannot be both Included and Excluded"))

        category = self.category
        another_card_with_same_category_exist = False
        card_with_same_category = frappe.get_all('Membership Card', filters={'membership_program': self.membership_program, 'category': category})

        for card in card_with_same_category:
            if card.name != self.name:
                another_card_with_same_category_exist = True
                break
        if another_card_with_same_category_exist:
            frappe.throw(_("Another card with same category already present"))

    def common_elements_in_lists(self, list1, list2, field_to_compare):
        for item1 in list1:
            for item2 in list2:
                if item1.get("field_to_compare") == item2.get("field_to_compare"):
                    return True

        return False
