from odoo import fields, models, api

from odoo.exceptions import ValidationError


class MyWork(models.Model):
    _name = "my.work"
    _inherit = "hr.employee"
    name = fields.Many2one('hr.employee', string='Người được đánh giá')
    job_id = fields.Many2one('hr.job', string='Chức vụ')
    department_id = fields.Many2one('hr.department', string="Phòng, ban")
    date_start = fields.Date(string='Ngày bắt đầu thử việc tại công ty', required=False, default=fields.Date.today)
    content = fields.Text(string='Nội dung thực hiện')
    level_participant = fields.Text(string='Mức độ tham gia')
    level_finish = fields.Float(string='Mức độ hoàn thành')
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
