# -*- coding: utf-8 -*-

{
    'name': "LIBRARY-P",
    'summary': """Library model""",
    'description': """Borrow Books Information""",
    'author': "Pv.info",
    'website': "https://pv.info",
    'category': 'Application',
    'version': '1.0',
    'depends': ['base','mail'],
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/muonsach_views.xml',
        'views/trasach_views.xml',
        'views/book_info_views.xml',
        'data/mail_template.xml',
        'data/mail_template_manager.xml',
        'data/return_approved_mail_template.xml',
        'data/return_request_mail_template.xml'
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}