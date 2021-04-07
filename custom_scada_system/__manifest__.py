
{
    'name': 'Scada Custmization',
    'version': '1.0',
    'category': '',
    'summary': 'Add some changes  to manufacturing',
    'description': "",
    'depends': ['base'
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/live_data.xml',
        'views/downtime_transaction.xml',
        'views/m_start_stop_view.xml',
        'views/production_speed_views.xml',
        'views/machine_capacity.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
