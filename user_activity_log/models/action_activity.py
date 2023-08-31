# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError, UserError
from odoo.http import request




class ActionActivity(models.Model):
    _name = 'action.activity'
    _description = "User's Action Activity"
    _order = 'date DESC'
    

    name = fields.Char('Name')
    user_id = fields.Many2one('res.users',string='User')
    action_id = fields.Many2one('ir.actions.actions', string='Actions Processes')
    date = fields.Datetime('Date & Time')
    binding_type = fields.Selection([('action', 'Action'),
                                     ('report', 'Report')],string='Type')
    ip = fields.Char('Latest IP Adress', size=15)
    
    
    