# -*- encoding: utf-8 -*-
{
    'name': 'test GD',
    'version': '19.0.1.0.0',
    'description': """Manage test""",

    'depends': [
        'base',
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
        'views/test_gd_module.xml',
        'views/column.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
