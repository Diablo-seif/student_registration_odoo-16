from odoo import models, fields, api
from datetime import date


class StudentRegistration(models.Model):
    _name = 'student.registration'
    _description = 'student.registration'
    _rec_name= "name_id"

    code = fields.Char(string='ID',required=True,default="New" )
    name_id = fields.Many2one(comodel_name="res.partner", required=True,domain=[('is_student','=',True)] )
    phone = fields.Char(related="name_id.phone" )
    age = fields.Integer(string="Age", compute="_compute_age", store=True, readonly=1 )
    date = fields.Date(string='Birth Date', related="name_id.birth_date")
    currency_id = fields.Many2one(comodel_name="res.currency",readonly=True,default = lambda self: self.env.company.currency_id,)
    amount = fields.Monetary(required=True)
    state = fields.Selection(selection=[    ('draft', 'Draft'),('confirmed', 'Confirmed'),('canceled', 'Canceled'),], required=False,default='draft' )

    def go_to_invoiced(self):
            print(self,"I want go to accounting")


    def bake_the_state(self):
        for rec in self:
            if rec.state in ['canceled','confirmed'] :
                rec.state = 'draft'
            elif rec.state == 'draft':
                rec.state = 'canceled'

    def move_the_state(self):
        for rec in self:
            if rec.state == 'draft' :
                rec.state = 'confirmed'


    @api.depends('date')
    def _compute_age(self):
        for rec in self:
            if rec.date:
                rec.age = (date.today() - rec.date).days // 365
            else:
                rec.age = 0

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('student.registration') or 'RG000000'

        student_name = ''
        if vals.get('name_id'):
            student = self.env['res.partner'].browse(vals['name_id'])
            student_name = student.name

        vals['code'] = f"{seq} - {student_name}"
        return super().create(vals)
