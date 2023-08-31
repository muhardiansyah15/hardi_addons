# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.home import Home as Hompage, LOGIN_SUCCESSFUL_PARAMS
from odoo.addons.web.controllers.utils import _get_login_redirect_url



_logger = logging.getLogger(__name__)


class HomeTermAndConditions(Hompage):

    def _login_redirect(self, uid, redirect=None):
        user = request.env['res.users'].browse(uid)
        if not user.tnc_acceptance:
            redirect = 'web/terms_and_conditions'
        return super()._login_redirect(uid, redirect=redirect)
    
    
    @http.route('/web/terms_and_conditions', type='http', auth='user', website=True, sitemap=False)
    def user_terms_and_conditions(self, **kwargs):
        valid_values = {k: v for k, v in kwargs.items() if k in LOGIN_SUCCESSFUL_PARAMS}
        user = request.env['res.users'].browse(request.session.uid)
        terms_content_html = user.company_id.terms_content_html or ''
        valid_values['terms_content_html'] = terms_content_html
        return request.render('user_terms_acceptance.web_login_terms_acceptance', valid_values)
    
    
    @http.route('/accepted_terms', type='http', auth='user', website=True, sitemap=False)
    def accepted_terms(self, **kwargs):
        user = request.env['res.users'].browse(request.session.uid)
        user.sudo().write({'tnc_acceptance': True})
        return request.redirect_query('/web', query=request.params)