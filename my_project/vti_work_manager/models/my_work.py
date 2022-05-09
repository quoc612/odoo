from odoo import fields, models, api

from odoo.exceptions import ValidationError


class MyWork(models.Model):
    _name = "my.work"
    _inherit = "hr.employee"
    name_people_review = fields.Many2many('hr.employee', string="Name of People Review")
    department_id = fields.Many2one('hr.employee', string='Department')
    job_id = fields.Many2one('hr.employee', string='Job Position')
    date_start = fields.Date('Start Date', required=True, default=fields.Date.today,
                             help="Start date of the contract.")
    reviewer = fields.Char('Reviewer')
    content = fields.Text(string='Content')
    level_participant = fields.Text('')
    level_finish = fields.Float('')
    quality = fields.Selection(
        [('excellent', 'Xuất sắc'), ('very_good', 'Tốt'), ('good', 'Khá'), ('average', 'Trung Bình'),
         ('bad', 'Chưa đạt, Tệ')])
    description = fields.Char()
    manager_description = fields.Char()
