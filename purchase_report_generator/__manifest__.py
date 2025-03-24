{
    'name': 'Purchase Dynamic Report Generator',
    'version': '17.0',
    'category': 'Purchase',
    'summary': """
        This module Helps to Generate All in One Dynamic Purchase Report
    """,
    'description': """
        This module facilitates comprehensive Purchase Reports, 
        offering insights into a company's procurement analysis from various 
        angles, including orders, order details, sales representatives, and the 
        ability to filter data by different date ranges.
     """,
    'depends': ['base', 'purchase'],
    'data': [
        'security/ir.model.access.csv',

        'views/dynamic_purchase_report_views.xml',

        'report/purchase_order_report_templates.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'purchase_report_generator/static/src/css/purchase_report.css',
            'purchase_report_generator/static/src/js/purchase_report.js',
            'purchase_report_generator/static/src/xml/purchase_report_view.xml',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
