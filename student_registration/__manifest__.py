{
    'name': "Students Registration",

    'summary': """
        Applications for registration of students""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','account','calendar'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/res_partner_inherit.xml',
        'views/accounting_move.xml',
        'views/menu.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
    'application': 'True'
}
