# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from odoo.http import request, route
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.addons.web.controllers.action import Action
from odoo import fields

_logger = logging.getLogger(__name__)


class ActionWeb(Action):
    
    @route('/web/action/load', type='json', auth="user")
    def load(self, action_id, additional_context=None):
        result = super().load(action_id, additional_context=additional_context)
        Actions = request.env['ir.actions.actions']
        binding_type = False
        base_action = Actions.browse([action_id]).sudo().read(['type'])
        if base_action:
            action_type = base_action[0]['type']
            action_binding_type = request.env[action_type].sudo().browse([action_id]).read(['binding_type'])
            if action_binding_type:
                binding_type = action_binding_type[0]['binding_type']
            
        if 'action.activity' in request.env:
            xml_id = 'access_action_activity'
            model_data = request.env['ir.model.data'].sudo().search([
                ('model', '=', 'ir.model.access'),
                ('module', '=', 'user_activity_log'),
                ('name', '=', xml_id),
            ])
            if model_data:
                
                request.env['action.activity'].sudo().create({
                            'name': request.env.user.name,
                            'user_id': request.env.uid,
                            'action_id': action_id,
                            'date': fields.datetime.now(),
                            'binding_type': binding_type  or False,
                            'ip': request.httprequest.headers.environ['REMOTE_ADDR'],
                        })
             
        return result