# -*- coding: utf-8 -*-
{
    'name': "Odoo Template Api",

    'summary': "Template odoo api",

    'description': """
This is template odoo api or example to create external api in odoo.
    """,

    'author': "Adrian Aji Septa",
    'website': "https://adrianajisepta.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

