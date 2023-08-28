# -*- coding: utf-8 -*-
{
    'name': "User Terms Acceptance",

    'summary': """
        The module facilitates the display of Terms and Conditions to users during the first login.""",

    'description': """
        The module facilitates the display of Terms and Conditions to users during the first login.
    """,

    'author': "Muhardiansyah",
    'website': "https://github.com/muhardiansyah15/hardi_addons",
    'category': 'Extra Tools',
    'version': '0.1',
    'depends': [
        'base',
        'web',
    ],

    'data': [
        'views/res_users_view.xml',
        'views/webclient_templates.xml',
    ],
    
    "assets": {
        "web.assets_frontend": [
            "/user_terms_acceptance/static/src/js/popup_tnc_acceptance.js",
        ]
    },

}
