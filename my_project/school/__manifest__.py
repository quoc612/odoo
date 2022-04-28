{

    'name': 'My Odoo',

    'version': '12.0.1.0.0',

    'summary': 'Record Student Information',

    'category': 'Tools',

    'author': 'Niyas Raphy',

    'maintainer': 'Cybrosys Techno Solutions',

    'company': 'Cybrosys Techno Solutions',

    'website': 'https://www.cybrosys.com',

    'depends': ['base', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/student_plus_view.xml',
        'security/student_right.xml',
        # 'views/button_send.xml',
        'views/test_email.xml',
    ],

    'images': [],

    'license': 'AGPL-3',

    'installable': True,

    'application': False,

    'auto_install': False,
}
