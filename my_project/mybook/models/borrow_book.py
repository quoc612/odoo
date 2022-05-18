from odoo import fields, api, models
from odoo.exceptions import ValidationError


class BorrowBook(models.Model):
    _name = "book.borrow"
    book_info_id = fields.Many2one('book.info', string="Book Info ID")
    name = fields.Char(string="Tên sinh viên")
    name_of_book = fields.Char(string="Các cuốn sách mượn")
    name_of_leader = fields.Char(string="Người quản lý")
    date_borrow_book = fields.Date(string="Ngày mượn sách")
    status_bar = fields.Selection([('draft', 'Draft'),
                                   ('confirm', 'Waiting Confirm'),
                                   ('approved', 'Approved')], string='Status', default='draft', index=True)

    @api.onchange("book_info_id")
    def check_borrow_book(self):
        self.name_of_book = self.book_info_id.name_of_book

    @api.multi
    def request_borrow_book(self):
        if self.status_bar == "draft":
            self.write({'status_bar': 'confirm'})
