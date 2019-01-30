# -*- coding: utf-8 -*-
{
    'name': "Student App",

    'summary': """
        Calculate your average""",

    'description': """
        Calculate the grade of your subjects with this module.
    """,

    'author': "Felipe Pineda",
    'website': "http://www.github.com/FelipePineda15",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}