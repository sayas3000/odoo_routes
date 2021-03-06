# -*- coding: utf-8 -*-
{
    'name': "Rutas Record",

    'summary': """
        Módulo de instalación de Rutas""",

    'description': """
        Instala Rutas Comerciales
    """,

    'author': "Isaías Carrillo Pérez",
    'website': "http://www.sdatos.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/client_routes.xml',
        #'views/order_clients.xml',
        #'views/order.xml',
        #'views/route_filter.xml'
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
        
    ],
    'installable': True,
    'auto_install': True,
}