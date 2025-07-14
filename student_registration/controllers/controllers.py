# -*- coding: utf-8 -*-
# from odoo import http


# class StudentRegistration(http.Controller):
#     @http.route('/student_registration/student_registration', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/student_registration/student_registration/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('student_registration.listing', {
#             'root': '/student_registration/student_registration',
#             'objects': http.request.env['student_registration.student_registration'].search([]),
#         })

#     @http.route('/student_registration/student_registration/objects/<model("student_registration.student_registration"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('student_registration.object', {
#             'object': obj
#         })
