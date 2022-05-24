from odoo import fields, models


class BookInfo(models.Model):
    _name = "book.info"


    name = fields.Char(string='Ten Sach', required=True)
    thoihan = fields.Integer(string='Thoi Han Tra Sach')
    heso = fields.Integer(string='He So Tra Muon', default=1)
    image = fields.Binary(string="Book Image", attachment=True, help="Book Image")
 #   _rec_name = 'name'

