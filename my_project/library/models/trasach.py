from odoo import fields, models, api
from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
class TraSach(models.Model):
    _name = "tra.sach"  # <- new model name
    _inherit = "muon.sach"

    name = fields.Many2one('muon.sach',string="Ten Sinh Vien")
    sachtra = fields.Many2one('book.info', string="Sach Tra")
    quanly = fields.Char(string='Nguoi Quan Ly', required=True)
    thoihan = fields.Integer(string='Thoi Han Tra Sach')
    heso = fields.Integer(string='He So Tra Muon')
    mail = fields.Char(string="Email")

    def _default_my_date(self):
        return fields.Date.context_today(self)
    ngaytra = fields.Date(string='Ngay Tra', default=_default_my_date)
    hantra = fields.Date(string="Han Tra")
    total_days = fields.Integer(string="TOTAL DAYS")

    @api.onchange('hantra', 'ngaytra', 'total_days')
    def calculate_date(self):
        if self.hantra and self.ngaytra:
            d1 = datetime.strptime(str(self.hantra), '%Y-%m-%d')
            d2 = datetime.strptime(str(self.ngaytra), '%Y-%m-%d')
            d3 = d2 - d1
            self.total_days = str(d3.days)

    tien = fields.Integer("Final Price", compute='_compute_final_price')
    @api.depends("total_days")
    def _compute_final_price(self):
        for record in self:
            record.tien = record.heso*record.total_days
            if record.tien <= 0:
                record.tien = 0

    @api.onchange('name')
    def x(self):
        if self.name:
            self.quanly = self.name.quanly
            self.hantra = self.name.hantra
            self.mail = self.name.mail

    @api.onchange('sachtra')
    def y(self):
        if self.sachtra:
            self.thoihan = self.sachtra.thoihan
            self.heso = self.sachtra.heso

    @api.one
    def started_progressbar(self):
        self.write({
            'state': 'request'
        })
        mail_template = self.env.ref('library.mail_template_tra')
        mail_template.send_mail(self.id, force_send=True)

    # This function is triggered when the user clicks on the button 'In progress'
    @api.one
    def progress_progressbar(self):
        self.write({
            'state': 'approving'
        })

    # This function is triggered when the user clicks on the button 'Done'
    @api.one
    def dones_progressbar(self):
        self.write({
            'state': 'done',
        })
        mail_template = self.env.ref('library.approved_mail_template_tra')
        mail_template.send_mail(self.id, force_send=True)
