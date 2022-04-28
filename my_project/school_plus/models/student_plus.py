from odoo import models, fields, api


class StudentStudentPlus(models.Model):
    _name = "super.student.student"
    _inherit = "student.student"

    toy = fields.Char('Pet Toy')
    age = fields.Integer('Pet Age', default=2)  # change default age from 1 to 2
    gender = fields.Selection(selection_add=[('sterilization', 'Sterilization')])  # add one more selection
    student_type = fields.Selection([('ok', 'not ok'), ('vip', 'VIP')], string='Student Type', default='ok')
