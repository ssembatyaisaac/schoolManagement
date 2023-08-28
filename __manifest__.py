# -*- coding: utf-8 -*-
{
    'name': "School Management",

    'summary': """
        Record Student Details""",

    'description': """
        To manage schools
    """,

    'author': "Ssembatya Isaac",
    'website': "https://ssembatyaisaac.github.io/",
    'company': "Ducky Technologies",
    'maintainer': 'Ssembatya Isaac',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': '',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

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
    'installable': True,
    'auto_install': False,
}
