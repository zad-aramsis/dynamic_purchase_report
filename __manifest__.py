{
    'name': "dynamic_purchase_report",
    'summary': """
        Dynamic Purchase Report
        """,
    'author': "",
    'website': "http://zadsolutions.com",
    'category': 'Purchase',
    'version': '17.0',
    'depends': ['base', 'purchase'],

    'data': [
        'security/ir.model.access.csv',

        'report/purchase_order_report.xml',
        'views/dynamic_purchase_report_views.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'dynamic_purchase_report/static/src/js/purchase_report_js.js',
            'dynamic_purchase_report/static/src/xml/purchase_report_xml.xml',
        ]
    },

    'installable': True,
    'auto_install': False,
    'application': False
}
