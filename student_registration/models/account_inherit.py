from odoo import models, fields, api


class PartnerInherit(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'


