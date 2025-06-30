from odoo import models, fields, api
from odoo.odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property'
    _description = 'property'
    _inherit=['mail.thread','mail.activity.mixin']

    name = fields.Char(string="Name", required=True,size=20 ,)
    code = fields.Integer(string="ID", required=True,)
    img = fields.Binary(string="    ",)
    owner_id = fields.Many2many(comodel_name="owner", inverse_name="property_id", string="Owner",tracking=1  )
    des = fields.Text(string="Description", required=False)
    postcode = fields.Char(string="Post Code", required=False)
    date_availability = fields.Datetime(string="Date Availability", required=False,tracking=1 )
    expected_price = fields.Float(string="Expected Price",  required=False)
    selling_price = fields.Float(string="Selling Price",  required=False  )
    bedrooms = fields.Integer(string="Bedrooms", default=False,  )
    kitchen = fields.Integer(string="kitchen", required=False,  )
    living_area = fields.Integer(string="Living Area", required=False )
    facades = fields.Integer(string="Facades", required=True,  )
    garage  = fields.Boolean(string="Garage", )
    garden  = fields.Boolean(string="Garden", )
    garden_area  = fields.Integer(string="", required=False, )
    garden_orientation = fields.Selection(string="Garden Orientation", selection=[('north', 'North'),
                                                                                  ('south', 'South'),
                                                                                  ('east' , 'East'),   ], required=False,default="north", )
    state = fields.Selection(string="State", selection=[('draft',    'Draft'),
                                                        ('pending', 'Pending'),
                                                        ('sold',    'Sold'), ], required=False,default="draft" ,tracking=1 )



    def change_state (self) :
        if  not self.state :
                        self.state = "draft"
        elif self.state == "draft":
                        self.state = "pending"
        elif self.state == "pending":
                        self.state = "sold"

    def back_state (self) :
        if   self.state == "draft":
                        self.state = False
        elif self.state == "pending":
                            self.state = "draft"
        elif self.state == "sold":
                        self.state = "pending"


    #
    #
    # @api.constrains('bedrooms')
    # def _check_bedrooms_greater_zero(self):
    #     # for rec in self :
    #         if self.bedrooms == 0  :
    #             raise ValidationError("Please write valid in number of bedrooms")
    #
    #



    # ,'living_area','kitchen','code','facades'
    #         elif rec.living_area == 0  :
    #             raise ValidationError("Please write valid in number of living_area")
    #         elif rec.kitchen == 0  :
    #             raise ValidationError("Please write valid in number of Kitchen")
    #         elif rec.code == 0  :
    #             raise ValidationError("Please write valid in number of Code")
    #         elif rec.facades == 0  :
    #             raise ValidationError("Please write valid in number of Facades")





