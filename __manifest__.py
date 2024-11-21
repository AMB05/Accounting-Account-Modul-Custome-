# # -*- coding: utf-8 -*-
# {
#     'name': "my_module_2",

#     'summary': "Short (1 phrase/line) summary of the module's purpose",

#     'description': """
# Long description of module's purpose
#     """,

#     'author': "My Company",
#     'website': "https://www.yourcompany.com",

#     # Categories can be used to filter modules in modules listing
#     # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
#     # for the full list
#     'category': 'Uncategorized',
#     'version': '0.1',

#     # any module necessary for this one to work correctly
#     'depends': ['base'],

#     # always loaded
#     'data': [
#         # 'security/ir.model.access.csv',
#         'views/views.xml',
#         'views/templates.xml',
#     ],
#     # only loaded in demonstration mode
#     'demo': [
#         'demo/demo.xml',
#     ],
# }

# my_module_2/__manifest__.py
{
    'name': 'My Module 2',
    'version': '3.3',
    'category': 'Accounting',
    'summary': 'Custom Accounting Module Example',
    'author': 'AMB',
    'website': 'https://www.doodex.net/',
    'depends': ['account'],  # Menambahkan dependensi ke modul 'account'
    'data': [
        'views/account_transaction_views.xml',  # Tampilan kustom untuk modul ini
        'security/ir.model.access.csv',  # File akses keamanan
        # 'models/account_transaction.py',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
