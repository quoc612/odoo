import datetime
import random
from datetime import date
from random import randint
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StudentStudent(models.Model):
    _name = 'student.student'
    _inherit = ['mail.thread']
    _rec_name = 'employee_id'
    # name = fields.Char(string='Name', required=False)
    employee_id = fields.Many2one('hr.employee', string='Employee')
    age = fields.Integer(string='Age')
    photo = fields.Binary(string='Image')
    quantity_of_pet = fields.Float()
    price_of_pet = fields.Float(compute="_compute_total")
    total = fields.Float(compute="_compute_total")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
    student_dob = fields.Date(string="Date of Birth")
    basic_point = fields.Float('Basic Point', default=0)
    student_blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        string='Blood Group')
    nationality = fields.Many2one('res.country', string='Nationality')
    company_id = fields.Many2one('res.company', string='Company')
    partner_id = fields.Many2one('res.partner', string='Partner')

    @api.onchange('student_dob')  # thay đổi thuộc tính của student_dob
    def calculateAge(self):
        if self.student_dob:
            today = date.today()
            age = today.year - self.student_dob.year - (
                    (today.month, today.day) < (self.student_dob.month, self.student_dob.day))
            self.age = age

    @api.constrains("quantity_of_pet")
    def _check_quantity(self):
        for record in self:
            if record.quantity_of_pet < 0:
                raise ValidationError("This fields not less than 0")

    @api.depends("quantity_of_pet", "age")
    def _compute_total(self):
        for records in self:
            records.price_of_pet = records.age * records.quantity_of_pet

    @api.multi
    def random(self):
        for record in self:
            record.student_dob = datetime.date(randint(1990, 2022), randint(1, 12), randint(1, 28))
            if record.student_dob:
                today = date.today()
                age = today.year - record.student_dob.year - (
                        (today.month, today.day) < (record.student_dob.month, record.student_dob.day))
                record.age = age
            gender = randint(1, 3)
            if gender == 1:
                record.gender = "male"
            elif gender == 2:
                record.gender = "female"
            elif gender == 3:
                record.gender = "others"
            record.quantity_of_pet = randint(1, 10)

    def action_send_email(self):
        self.ensure_one()
        mail_template = self.env.ref('school.email_template')
        mail_template.send_mail(self.id, force_send=True)

    # _inherit = 'res.partner'

    @api.multi
    def send_mail_template(self):
        # Find the e-mail template
        template = self.env.ref('mail_template_demo.example_email_template')
        # You can also find the e-mail template like this:
        # template = self.env['ir.model.data'].get_object('mail_template_demo', 'example_email_template')

        # Send out the e-mail template to the user
        self.env['mail.template'].browse(template.id).send_mail(self.id)
