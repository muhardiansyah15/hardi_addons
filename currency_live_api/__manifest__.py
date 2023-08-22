# -*- coding: utf-8 -*-
{
    'name': "Currency Exchange Rate API",

    'summary': """
        Import exchange rates from the providers.""",

    'description': """
        Import exchange rates from the providers.
    """,

    'author': "Muhardiansyah",
    'website': "https://github.com/muhardiansyah15",
    'category': 'Accounting/Accounting',
    'version': '0.1',
    'depends': [
        'account',
    ],
    'data': [
        'views/res_config_settings_views.xml',
        'views/service_cron_data.xml',
        'data/data.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'OEEL-1',

}
