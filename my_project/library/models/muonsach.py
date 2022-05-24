from odoo import fields, models,api
from datetime import date, datetime




class MuonSach(models.Model):
    _name = "muon.sach"
    _inherit = "book.info"

    name = fields.Char(string='Ten Sinh Vien', required=True)
    quanly = fields.Char(string='Nguoi Quan Ly', required=True)
    ngaymuon = fields.Date(string='Ngay Muon', required=True, default=datetime.now().strftime('%Y-%m-%d'))
    sachmuon = fields.Many2one('book.info', string="Sach Muon")
    mail = fields.Char(string="Email")
    hantra = fields.Date(string='Han Tra')
    @api.onchange('sachmuon')
    def _default_my_date(self):
        if self.sachmuon:
            self.hantra = self.ngaymuon + relativedelta(months=self.sachmuon.thoihan)

    state = fields.Selection([

        ('request', 'Request'),
        ('approving', 'approving'),
        ('done', 'Done'),
    ], default='request')



    # This function is triggered when the user clicks on the button 'Set to started'
    @api.one
    def started_progressbar(self):
        self.write({
            'state': 'request'
        })
        mail_template = self.env.ref('library.mail_template')
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
        mail_template = self.env.ref('library.mail_template_manager')
        mail_template.send_mail(self.id, force_send=True)






