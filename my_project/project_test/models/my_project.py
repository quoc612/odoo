from odoo import api, fields, models, tools, _

from odoo.exceptions import UserError, ValidationError


class MyProject(models.Model):
    _name = "my.project"
    _description = "My Project Model"

    name = fields.Char('Name', required=True)
    age = fields.Integer('Age', default=1)
    weight = fields.Float('Weight (kg)')
