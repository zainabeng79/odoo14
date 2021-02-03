# -*- coding: utf-8 -*-
{
    'name': "Web Maintenance Ticket",

    'summary': """
        Web Maintenance Ticket""",

    'description': """
        Web Maintenance Ticket
    """,

    'author': "M Said",
    'website': "http://www.yourcompany.com",

    'category': 'maintenance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['maintenance', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
