# -*- coding: utf-8 -*-
# from odoo import http


# class UserTermsAcceptance(http.Controller):
#     @http.route('/user_terms_acceptance/user_terms_acceptance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/user_terms_acceptance/user_terms_acceptance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('user_terms_acceptance.listing', {
#             'root': '/user_terms_acceptance/user_terms_acceptance',
#             'objects': http.request.env['user_terms_acceptance.user_terms_acceptance'].search([]),
#         })

#     @http.route('/user_terms_acceptance/user_terms_acceptance/objects/<model("user_terms_acceptance.user_terms_acceptance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('user_terms_acceptance.object', {
#             'object': obj
#         })
