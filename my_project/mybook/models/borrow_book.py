from odoo import fields, api, models
from odoo.exceptions import ValidationError


class BorrowBook(models.Model):
    _name = "book.borrow"
    book_info_id = fields.Many2one('book.info', string="Book Info ID")
    name = fields.Char(string="Tên sinh viên")
    name_of_book = fields.Char(string="Tên sách")
    is_expried_of_book = fields.Float(string="Thời hạn trả sách", default=2)
    number_of_money = fields.Float(string="Hệ số tính tiền trả muộn", default=5000)
    name_of_leader = fields.Char(string="Người quản lý")
    date_borrow_book = fields.Date(string="Ngày mượn sách")
    borrow_book_list = fields.Char(string="Các cuốn sách mượn")
    status_bar = fields.Selection([('draft', 'Draft'),
                                   ('confirm', 'Waiting Confirm'),
                                   ('approved', 'Approved')], string='Status', default='draft', index=True)
    # check_button = fields.Boolean(compute='check_permisson')

    @api.multi
    def request_borrow_book(self):
        if self.status_bar == "draft":
            self.write({'status_bar': 'confirm'})

    # @api.depends("check_button")
    # def check_button(self):
    #     if self.env


