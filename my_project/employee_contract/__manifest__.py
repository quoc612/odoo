{

    'name': 'My Contract',

    'version': '1234',

    'summary': 'My Odoo',

    'category': 'Tools',

    'author': 'Niyas Raphy',

    'maintainer': 'My Odoo',

    'company': 'My Odoo',

    'website': 'https://www.cybrosys.com',

    'depends': ['base', 'mail', 'hr_contract'],

    'data': [
        'security/ir.model.access.csv',
        'views/my_contract.xml',

    ],

    'images': [],

    'license': 'AGPL-3',

    'installable': True,

    'application': False,

    'auto_install': False,
}
