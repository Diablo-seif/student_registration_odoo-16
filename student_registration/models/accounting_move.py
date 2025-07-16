from odoo import models, fields, api


class AccountingMove(models.Model):
    _inherit = 'account.move'
    registration_id = fields.Many2one(comodel_name="student.registration", required=False)


    def go_to_student(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Student Registration',
            'res_model': 'student.registration',
            'view_mode': 'tree,form',
            'target': 'current',
        }
