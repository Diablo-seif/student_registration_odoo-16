# -*- coding: utf-8 -*-
# from odoo import http


# class Max(http.Controller):
#     @http.route('/max/max', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/max/max/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('max.listing', {
#             'root': '/max/max',
#             'objects': http.request.env['max.max'].search([]),
#         })

#     @http.route('/max/max/objects/<model("max.max"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('max.object', {
#             'object': obj
#         })
