# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class user_terms_acceptance(models.Model):
#     _name = 'user_terms_acceptance.user_terms_acceptance'
#     _description = 'user_terms_acceptance.user_terms_acceptance'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
