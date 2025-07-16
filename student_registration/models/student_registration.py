from odoo import models, fields, api
from datetime import date


class StudentRegistration(models.Model):
    _name = 'student.registration'
    _description = 'student.registration'
    _rec_name= "name_id"

    code = fields.Char(string='ID',required=True,default="New",readonly=True )
    name_id = fields.Many2one(comodel_name="res.partner", required=True,domain=[('is_student','=',True)] )
    phone = fields.Char(related="name_id.phone" )
    age = fields.Integer(string="Age", compute="_compute_age", store=True, readonly=1 )
    date = fields.Date(string='Birth Date', related="name_id.birth_date")

    currency_id = fields.Many2one(comodel_name="res.currency",readonly=True,default = lambda self: self.env.company.currency_id,)

    amount = fields.Monetary(required=True)
    state = fields.Selection(selection=[    ('draft', 'Draft'),('confirmed', 'Confirmed'),('canceled', 'Canceled'),], required=False,default='draft' )
    # I want to calculate invoice counts for user by _compute_invoice_count in fields integer (invoice_count)
    invoice_count = fields.Integer(string="Invoice Count", compute='_compute_invoice_count',readonly=True)

    def action_create_invoice(self):
        for rec in self:
            invoice_vals = {
                'move_type': 'out_invoice',
                'partner_id': rec.name_id.id,
                'currency_id': rec.currency_id.id,
                'invoice_line_ids': [
                    (0, 0, {
                        'name': f'Student Registration - {rec.code}',
                        'quantity': 1,
                        'price_unit': rec.amount,
                    })
                ],
            }
            invoice = self.env['account.move'].create(invoice_vals)
            return {
                'name': 'Invoice',
                'view_mode': 'form',
                'res_model': 'account.move',
                'res_id': invoice.id,
                'type': 'ir.actions.act_window',
            }

    def go_to_invoiced(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoices',
            'res_model': 'account.move',
            'view_mode': 'tree,form',
            'domain': [('partner_id', '=', self.name_id.id), ('move_type', '=', 'out_invoice')],
        }

    # to know how many (invoice count) for user
    def _compute_invoice_count(self):
            for rec in self:
                if rec.name_id:
                    rec.invoice_count = self.env['account.move'].search_count([
                        ('partner_id', '=', rec.name_id.id),
                        ('move_type', '=', 'out_invoice'),
                    ])
                else:
                    rec.invoice_count = 0


    # make bottoms for bake the state
    def bake_the_state(self):
        for rec in self:
            if rec.state in ['canceled','confirmed'] :
                rec.state = 'draft'
            elif rec.state == 'draft':
                rec.state = 'canceled'

    # make bottoms for move the state
    def move_the_state(self):
        for rec in self:
            if rec.state == 'draft' :
                rec.state = 'confirmed'


    # calculate of age by date
    @api.depends('date')
    def _compute_age(self):
        for rec in self:
            if rec.date:
                rec.age = (date.today() - rec.date).days // 365
            else:
                rec.age = 0

    # automatic code by (RX000001 - name_id)
    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('student.registration') or 'RG000000'
        student_name = 'New'

        if vals.get('name_id'):
            student = self.env['res.partner'].browse(vals['name_id'])
            student_name = student.name

        vals['code'] = f"{seq} - {student_name}"
        return super().create(vals)
