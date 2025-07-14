from odoo import models, fields, api


class AccountingMove(models.Model):
    _inherit = 'account.move'
    registration_id = fields.Many2one(comodel_name="student.registration", required=False)

    def go_to_student (self):
        print(self, "I want go to student")
