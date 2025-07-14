from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class PartnerInherit(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean(string="Is Student", default=True )
    birth_date = fields.Date(string="birth date", )
    @api.constrains ('birth_date')
    def _check_birth_date(self):
        for rec in self :
            if rec.birth_date and rec.birth_date > date.today():
                raise ValidationError("Birth date must be in the past.")

