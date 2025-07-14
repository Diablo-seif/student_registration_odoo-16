from odoo import models, fields, api


class TeamCourse(models.Model):
    _name = 'team.course'
    _description = 'team.course'

    name = fields.Char()
