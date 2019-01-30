# -*- coding: utf-8 -*-
from openerp import http

# class Estudiantes(http.Controller):
#     @http.route('/estudiantes/estudiantes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estudiantes/estudiantes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('estudiantes.listing', {
#             'root': '/estudiantes/estudiantes',
#             'objects': http.request.env['estudiantes.estudiantes'].search([]),
#         })

#     @http.route('/estudiantes/estudiantes/objects/<model("estudiantes.estudiantes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estudiantes.object', {
#             'object': obj
#         })