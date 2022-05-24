from dateutil.relativedelta import relativedelta

from odoo import fields, api, models
from odoo.exceptions import ValidationError


class BorrowBook(models.Model):
    _name = "book.borrow"
    _inherit = "book.info"
    book_info_id = fields.Many2one('book.info', string="Book Info ID")
    name = fields.Char(string="Tên sinh viên")
    name_of_book = fields.Char(string="Các cuốn sách mượn")
    name_of_leader = fields.Char(string="Người quản lý")
    date_borrow_book = fields.Date(string="Ngày mượn sách")
    is_expried_of_book = fields.Char(string='Thời hạn trả sách')
    date_return_expried = fields.Date(string="Hạn trả", compute='_compute_deadline')
    email = fields.Char(string="Email")
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Waiting Confirm'),
                              ('approved', 'Approved')], string='Status', default='draft', index=True)

    @api.onchange("book_info_id")
    def check_borrow_book(self):
        self.name_of_book = self.book_info_id.id

    @api.onchange("book_info_id")
    def check_borrow_book(self):
        self.is_expried_of_book = self.book_info_id.is_expried_of_book
    @api.depends("date_borrow_book",'is_expried_of_book')
    def _compute_deadline(self):
        for re in self:
            if re.date_borrow_book and re.is_expried_of_book:
                re.date_return_expried = re.date_borrow_book + relativedelta(months=re.book_info_id.is_expried_of_book)

    @api.one
    def started_progressbar(self):
        if self.state == "draft":
            self.write({'state': 'confirm'})
            mail_template = self.env.ref('mybook.mail_templates')
            mail_template.send_mail(self.id, force_send=True)

    @api.one
    def confirm_progressbar(self):
        if self.state == "confirm":
            self.write({'state': 'approved'})
            mail_template = self.env.ref('mybook.mail_borrow_accept')
            mail_template.send_mail(self.id, force_send=True)
