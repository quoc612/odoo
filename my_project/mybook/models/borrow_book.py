from odoo import fields, api, models
from odoo.exceptions import ValidationError


class BorrowBook(models.Model):
    _name = "book.borrow"
    name = fields.Char(string="Tên sinh viên")
    name_of_leader = fields.Char(string="Người quản lý")
    date_borrow_book = fields.Date(string="Ngày mượn sách")
    borrow_book_list = fields.Char(string="Các cuốn sách mượn")
    
