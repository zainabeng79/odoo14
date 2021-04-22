{
    'name': 'MRP Custmization',
    'version': '1.0',
    'category': '',
    'summary': 'Add some changes  to maintenance',
    'description': "",
    'depends': ['maintenance','web'
                ],
    'data': [
        'views/mrp_request_view.xml',
        'report/mrpreq_report.xml',
             ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
