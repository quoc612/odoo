from odoo import fields, api, models
from odoo.exceptions import ValidationError


class ReturnBook(models.Model):
    _name = "book.return"
    _inherit = "book.info"
    book_borrow_id = fields.Many2one('book.borrow', string="Book borrow ID")
    name = fields.Char(string="Tên sinh viên")
    name_of_leader = fields.Char(string="Người quản lý")
    borrow_book_list = fields.Char(string="Các cuốn sách trả")
    date_borrow_book = fields.Date(string="Ngày trả sách")
    total_late_book = fields.Float(string="Tổng tiền trả muộn")

    @api.onchange("book_borrow_id")
    def show_list(self):
        self.name = self.book_borrow_id.name
        self.name_of_leader = self.book_borrow_id.name_of_leader
        self.date_borrow_book = self.book_borrow_id.date_borrow_book

    # @api.onchange("total_late_book")
    # def total_late(self):
    #     self.total_late_book = self.
