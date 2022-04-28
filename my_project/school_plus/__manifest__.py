{

    'name': 'My Odoo Plus',

    'version': '12.0.1.0.0',

    'summary': 'Record Student Information',

    'category': 'Tools',

    'author': 'Niyas Raphy',

    'maintainer': 'Cybrosys Techno Solutions',

    'company': 'Cybrosys Techno Solutions',

    'website': 'https://www.cybrosys.com',

    'depends': ['school'],

    'data': [
        'security/ir.model.access.csv',
        'views/student_plus_view.xml',
        'views/product_student_view.xml',
    ],

    'images': [],

    'license': 'AGPL-3',

    'installable': True,

    'application': False,

    'auto_install': False,
}
