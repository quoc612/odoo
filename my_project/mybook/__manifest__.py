{
    'name': "Book Managerment",
    'version': '1.0',
    'depends': ['base', 'hr','mail'],
    'author': "VTI",
    'category': 'Category',
    'description': "",
    'data': [
        'security/ir.model.access.csv',
        'security/security_main.xml',
        'views/my_book.xml',
        'views/borrow_book.xml',
        'views/return_book.xml',
        'data/mail_template.xml',
        'data/mail_borrow_accept.xml'
    ],
    'demo': [],
}
