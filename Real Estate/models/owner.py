from odoo import models, fields, api

class Owner(models.Model):
    _name = 'owner'
    _description = 'owner'

    name = fields.Char(string="Name", required=True)
    img = fields.Binary(string="    ")
    property_id = fields.Many2many(comodel_name="property", string="property", )


