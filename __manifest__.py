# -*- encoding: utf-8 -*-
{
    'name': 'test',
    'version': '19.0',
    'description': """Manage test""",

    'depends': [
        'base',
        'contacts',
    ],
    'data': [
        # assets
        # models

        # fields
        # actions
        # reports
        # security
        'security/ir.model.access.csv',
        # views
        'views/test_module.xml',
        'views/outage.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
}
