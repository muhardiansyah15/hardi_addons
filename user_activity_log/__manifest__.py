# -*- coding: utf-8 -*-
{
    'name': "User Activity Log",
    'summary': 'Enhance security and transparency by tracking user activities and IP addresses in Odoo.',
    'description': 'The "User Activity Log" module enables comprehensive tracking of user actions and IP addresses in the Odoo system. Enhance security, transparency, and accountability.',
    'author': "Muhardiansyah",
    'website': "https://github.com/muhardiansyah15/hardi_addons",
    'category': 'Tools/Tools',
    'license': 'AGPL-3',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/action_activity_view.xml',
    ],
}
