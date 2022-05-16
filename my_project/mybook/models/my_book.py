import datetime

from odoo import fields, api, models
from odoo.exceptions import ValidationError


class BookInfo(models.Model):
    _name = "my.book.info"

    name_of_book = fields.Char(string="Tên sách")
    is_expried_of_book = fields.Float(string="Thời hạn trả sách")
    number_of_money = fields.Float(string="Hệ số tính tiền trả muộn")

#
# class BorrowBook(models.Model):
#     _name = "my.book.borrow"
#     _inherit = 'hr.employee'
#     name_of_student = fields.Char(string="Tên sinh viên")
#     name_of_leader = fields.Many2one('hr.employee', string="Tên người quản lý")
#     book_borrow_day = fields.Date(string="Ngày mượn sách")
#     list_of_book = fields.Text(string="Các cuốn sách mượn")
#
#
# class ReturnBook(models.Model):
#     _inherit = "my.book.borrow"
#     _name = "my.book.return"
#     name_of_student = fields.One2many('my.book.borrow', string="Tên sinh viên")
#     name_of_leader = fields.Many2one('hr.employee', string="Tên người quản lý")
#     list_of_book = fields.Text(string="Các cuốn sách mượn")
#     book_return_day = fields.Date(string="Ngày trả sách")
#     total = fields.Float(string="Tổng tiền trả muộn")
