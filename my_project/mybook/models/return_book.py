from odoo import fields, api, models
from odoo.exceptions import ValidationError
from datetime import datetime
from dateutil.relativedelta import relativedelta


class ReturnBook(models.Model):
    _name = "book.return"
    book_borrow_id = fields.Many2one('book.borrow', string="Book borrow ID")
    name = fields.Char(string="Tên sinh viên")
    name_of_leader = fields.Char(string="Người quản lý")
    name_of_book = fields.Char(string="Các cuốn sách mượn")
    date_borrow_book = fields.Date(string="Ngày trả sách")
    is_expried_of_book = fields.Date(string='Thời hạn trả sách')
    # date_return_expried = fields.Date(string="Hạn trả", compute='_compute_deadline')
    total_late_book = fields.Integer(string="Tổng tiền trả muộn")
    email = fields.Char(string="Email")
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Waiting Confirm'),
                              ('approved', 'Approved')], string='Status', default='draft', index=True)

    @api.onchange("book_borrow_id")
    def show_list(self):
        self.name = self.book_borrow_id.name
        self.name_of_leader = self.book_borrow_id.name_of_leader
        self.date_borrow_book = self.book_borrow_id.date_borrow_book
        self.name_of_book = self.book_borrow_id.name_of_book

    # def _compute_deadline(self):
    #     @api.depends("date_borrow_book", 'is_expried_of_book')
    #     def _compute_deadline(self):
    #         for re in self:
    #             if re.date_borrow_book and re.is_expried_of_book:
    #                 re.date_return_expried = re.date_borrow_book + relativedelta(
    #                     months=re.book_info_id.is_expried_of_book)
    #
    # @api.onchange('hantra', 'ngaytra', 'total_days')
    # def calculate_date(self):
    #     if self.hantra and self.ngaytra:
    #         d1 = datetime.strptime(str(self.hantra), '%Y-%m-%d')
    #         d2 = datetime.strptime(str(self.ngaytra), '%Y-%m-%d')
    #         d3 = d2 - d1
    #         self.total_days = str(d3.days)
    #
    # tien = fields.Integer("Final Price", compute='_compute_final_price')
    #
    # @api.depends("total_days")
    # def _compute_final_price(self):
    #     for record in self:
    #         record.tien = record.heso * record.total_days
    #         if record.tien <= 0:
    #             record.tien = 0
    #
    # @api.onchange('name')
    # def x(self):
    #     if self.name:
    #         self.quanly = self.name.quanly
    #         self.hantra = self.name.hantra
    #         self.mail = self.name.mail
    #
    # @api.onchange('sachtra')
    # def y(self):
    #     if self.sachtra:
    #         self.thoihan = self.sachtra.thoihan
    #         self.heso = self.sachtra.heso
