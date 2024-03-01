# -*- coding: utf-8 -*-
{
    'name': "tcm_client",

    'summary': "Client app for TCM",

    'description': """
Client app for TCM
    """,

    'author': "Computs Sdn Bhd",
    'website': "https://www.computs.com.my",
    'application': True,
    'sequence': -999,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/client_subscription.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

