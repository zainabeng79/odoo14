# -*- coding: utf-8 -*-
# from odoo import http


# class ExtendMaintenance(http.Controller):
#     @http.route('/extend_maintenance/extend_maintenance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extend_maintenance/extend_maintenance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extend_maintenance.listing', {
#             'root': '/extend_maintenance/extend_maintenance',
#             'objects': http.request.env['extend_maintenance.extend_maintenance'].search([]),
#         })

#     @http.route('/extend_maintenance/extend_maintenance/objects/<model("extend_maintenance.extend_maintenance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extend_maintenance.object', {
#             'object': obj
#         })
