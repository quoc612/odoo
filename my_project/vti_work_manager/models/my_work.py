from odoo import fields, models, api

from odoo.exceptions import ValidationError


class MyWork(models.Model):
    _name = "my.work"
    _inherit = "hr.employee"
    employee_name = fields.Many2many('hr.employee', string="Người được đánh giá")
    position_id = fields.Many2one('hr.employee', string='Chức vụ')
    # department_id = fields.Many2one('hr', string='Phòng ban')
    date_start = fields.Date('Ngày bắt đầu thử việc tại công ty', required=True, default=fields.Date.today,
                             help="Start date of the contract.")
    reviewer = fields.Text(string='Người đánh giá')
    content = fields.Text(string='Nội dung thực hiện')
    level_participant = fields.Text('Mức độ tham gia')
    level_finish = fields.Float('')
    quality_review = fields.Selection(
        [('excellent', 'Xuất sắc'), ('very_good', 'Tốt'), ('good', 'Khá'), ('average', 'Trung Bình'),
         ('bad', 'Chưa đạt, Tệ')])
    note = fields.Text(string="Ghi chú")
    manager_description = fields.Text(string="Quản lý trực tiếp đánh giá")
    personal_review = fields.Float(string="Cá nhân tự đánh giá")
    manager_review = fields.Float(string="Quản lý đánh giá")
    note_review = fields.Text(string="Ghi chú")
    total_review = fields.Float(string="Tổng điểm")
    request_review = fields.Text(string="Ý kiến, kiến nghị")
    comment_review = fields.Text(string="Ý kiến, nhận xét")

    @api.constrains('level_finish')
    def check_level_finish(self):
        for records in self:
            if records.level_finish > 100:
                raise ValidationError("Chỉ nhập nhỏ hơn 100%")

    @api.constrains('total_review')
    def total_review(self):
        for rec in self:
            rec.total_review = rec.level_finish * rec.personal_review

        # self.total_review = total_review
