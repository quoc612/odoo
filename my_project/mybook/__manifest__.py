{
    'name': "Book Managerment",
    'version': '1.0',
    'depends': ['base', 'hr', 'mail'],
    'author': "VTI",
    'category': 'Category',
    'description': "",
    'data': [
        'data/mail_template.xml',
        'data/mail_borrow_accept.xml',
        'security/security_main.xml',
        'security/ir.model.access.csv',
        'views/return_book.xml',
        'views/borrow_book.xml',
        'views/my_book.xml',
    ],
    'demo': [],
}
