from odoo import models, fields, api


class ProductStudent(models.Model):
    _name = "product.student"
    _inherit = 'student.student'
    student_student_id = fields.Many2one('student.student', auto_join=True, index=True, ondelete="cascade",
                                         required=True)
    student_type = fields.Selection([('ok', 'not ok'), ('vip', 'VIP')], string='Student Type', default='ok')
    color = fields.Selection([('white', 'White'), ('black', 'Black')], string='Color', default='black')
    bonus_point_1 = fields.Float("Bonus Point", default=0)
    bonus_point = fields.Float("Final Point", compute='_compute_final_point', store=True)

    @api.depends('bonus_point', 'basic_point')
    def _compute_final_point(self):
        for point in self:
            point.final_point = point.bonus_point + point.basic_point
