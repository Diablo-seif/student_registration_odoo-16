# -*- coding: utf-8 -*-
# from odoo import http


# class GradHub(http.Controller):
#     @http.route('/grad_hub/grad_hub', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/grad_hub/grad_hub/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('grad_hub.listing', {
#             'root': '/grad_hub/grad_hub',
#             'objects': http.request.env['grad_hub.grad_hub'].search([]),
#         })

#     @http.route('/grad_hub/grad_hub/objects/<model("grad_hub.grad_hub"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('grad_hub.object', {
#             'object': obj
#         })
