{
    'name': 'MRP Custmization',
    'version': '1.0',
    'category': '',
    'summary': 'Add some changes  to maintenance',
    'description': "",
    'depends': ['maintenance','web','purchase'
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/maintenance_checklist.xml',
        'views/mrp_request_view.xml',
        'report/mrpreq_report.xml',
        'views/insurance.xml',
        'views/test.xml',
             ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
