from odoo import fields, api, models
from odoo.exceptions import ValidationError


class BorrowBook(models.Model):
    _name = "book.borrow"
    book_info_id = fields.Many2one('book.info', string="Book Info ID")
    name = fields.Char(string="Tên sinh viên")
    name_of_book = fields.Char(string="Các cuốn sách mượn")
    name_of_leader = fields.Char(string="Người quản lý")
    date_borrow_book = fields.Date(string="Ngày mượn sách")
    email = fields.Char(string="Email")
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Waiting Confirm'),
                              ('approved', 'Approved')], string='Status', default='draft', index=True)

    @api.onchange("book_info_id")
    def check_borrow_book(self):
        self.name_of_book = self.book_info_id.name_of_book

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
