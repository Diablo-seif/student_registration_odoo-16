from odoo import models, fields, api

class Sale(models.Model):
    _inherit="sale.order"
    owner_id = fields.Many2many(comodel_name="owner",inverse_name="property_id", string="Owner", required=False, )