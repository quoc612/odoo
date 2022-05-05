from odoo import fields, api, models
from datetime import date

from odoo.exceptions import ValidationError


class MyContract(models.Model):
    _inherit = 'hr.contract'

    # state = fields.Selection([
    #     ('draft', 'New'),
    #     ('open', 'Running'),
    #     ('pending', 'To Renew'),
    #     ('close', 'Expired'),
    #     ('cancel', 'Cancelled')
    # ], string='Status', group_expand='_expand_states',
    #     track_visibility='onchange', help='Status of the contract', default='draft')

    # contract_id = fields.Char(string="Contract ID", required=True)
    # # department_id = fields.Many2one('hr.department', string="Department")
    # # employee_id = fields.Many2one('hr.contract', string='Employee')
    # date_start = fields.Date(string="Date Start", required=True, default=date.today())
    # date_end = fields.Date(string="Date End", required=True)
    # name = fields.Char(string='Employee Name')
    @api.multi
    def btn_waiting_approval(self):
        if self.state == "draft":
            self.write({'state': 'open'})
            mail_template = self.env.ref('employee_contract.email_template_contract')
            mail_template.send_mail(self.id, force_send=True)
            return {
                'name': 'Success'

            }
        elif self.state == "cancel":
            self.write({'state': 'draft'})

    @api.multi
    def btn_cancel_approval(self):
        if self.state == "open":
            self.write({'state': 'cancel'})
        else:
            self.write({'state': 'draft'})


